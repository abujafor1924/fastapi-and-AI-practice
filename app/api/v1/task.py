# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.crud.task import create_task, get_task, get_user_tasks, update_task, delete_task
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
    # --- QUERY PARAMETERS DEMO ---
    # In Django: You fetch query params via `request.GET.get('skip')` or `request.query_params.get('skip')`.
    #            You must manually convert them from string to integer and handle validation/casting exceptions yourself.
    # In FastAPI: Declaring parameters that are not part of the route URL template and are primitive types (like int, str)
    #             tells FastAPI to parse them from the URL query string automatically (e.g. ?skip=10&limit=5).
    #             The Query() class adds extra validation constraints (like ge=0, le=100) and describes them for Swagger.
    skip: int = Query(default=0, ge=0, description="Pagination skip (offset) value. Must be greater than or equal to 0."),
    limit: int = Query(default=100, ge=1, le=100, description="Pagination limit (size) value. Range: 1-100."),
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
    # --- PATH PARAMETERS DEMO ---
    # In Django: Configured in urls.py (e.g. `path('tasks/<int:task_id>/')`) and passed as arguments to the view function.
    # In FastAPI: You declare variables in curly braces in the route path `@router.get("/{task_id}")`.
    #             FastAPI inspects the route parameters and automatically maps them to function arguments with the same name.
    #             The Path() helper lets us enforce validation constraints (e.g., ID must be greater than or equal to 1).
    task_id: int = Path(..., ge=1, description="The unique database ID of the task to retrieve."),
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

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Updates the title and/or description of a specific task.
    Enforces security: Users cannot update tasks belonging to other users.
    Invalidates the user's tasks cache in Redis.
    """
    db_task = get_task(db, task_id)
    if not db_task or db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )
    
    updated_db_task = update_task(db, task_id, task_update)
    cache.delete(f"user_tasks:{current_user.id}:0:100")
    return updated_db_task

@router.delete("/{task_id}")
def delete_task_endpoint(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Deletes a specific task.
    Enforces security: Users cannot delete tasks belonging to other users.
    Invalidates the user's tasks cache in Redis.
    """
    db_task = get_task(db, task_id)
    if not db_task or db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )
    
    delete_task(db, task_id)
    cache.delete(f"user_tasks:{current_user.id}:0:100")
    return {"message": "Task deleted successfully"}

