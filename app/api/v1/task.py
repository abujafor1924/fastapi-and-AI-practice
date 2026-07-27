from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse
from app.crud.task import create_task, get_task, get_user_tasks
from app.tasks.background_tasks import process_heavy_task
from app.core.cache import cache

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# --- TASK API ENDPOINTS ---

@router.post("/", response_model=TaskResponse, status_code=201)
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Creates a new background task for the authenticated user.
    1. Saves the task in PostgreSQL (status is queued).
    2. Offloads the execution to Celery using '.delay()'.
    3. Invalidates the user's tasks cache in Redis (ensures they see the new task on next GET).
    """
    # 1. DB Save
    db_task = create_task(db, task, user_id=current_user.id)
    
    # 2. Celery Dispatch
    # .delay() is a shortcut to send a task message to the broker (Redis)
    process_heavy_task.delay(db_task.id)
    
    # 3. Cache Invalidation
    # We clear the list cache so the user gets updated data on their next request
    cache.delete(f"user_tasks:{current_user.id}:0:100")
    
    # Refresh the task object to pull the latest state (e.g., if worker ran eagerly in tests)
    db.refresh(db_task)
    
    return db_task


@router.get("/", response_model=list[TaskResponse])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Fetches all tasks created by the current user.
    Implements Cache-Aside Pattern:
    - Checks Redis first (Cache Hit). If found, returns it immediately (super fast).
    - If not in Redis (Cache Miss), queries PostgreSQL, caches the result in Redis, and returns it.
    """
    cache_key = f"user_tasks:{current_user.id}:{skip}:{limit}"
    
    # 1. Check Redis Cache
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        # Cache Hit! Return the cached JSON directly
        return cached_data
        
    # 2. Cache Miss: Fetch from PostgreSQL
    tasks = get_user_tasks(db, user_id=current_user.id, skip=skip, limit=limit)
    
    # 3. Serialize SQLAlchemy models into JSON-compatible format for Redis
    serialized_tasks = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "result": task.result,
            "user_id": task.user_id,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat()
        }
        for task in tasks
    ]
    
    # 4. Save to Redis Cache with 60-second TTL (Time to Live)
    cache.set(cache_key, serialized_tasks, expire_seconds=60)
    
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve the status and results of a specific task.
    Enforces security: Users cannot query tasks belonging to other users.
    """
    db_task = get_task(db, task_id)
    if not db_task or db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )
    return db_task
