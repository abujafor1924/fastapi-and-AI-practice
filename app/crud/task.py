from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


# --- TASK CRUD OPERATIONS ---
# Handles the direct interaction with the PostgreSQL database for the Task model.
# By isolating database access here, we keep our API route handlers clean and testable.

def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
    """
    Creates a new Task record in the database for a specific user.
    Starts with the 'queued' status by default.
    """
    db_task = Task(
        title=task.title,
        description=task.description,
        user_id=user_id,
        status="queued"
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)  # Refreshes the instance to load DB-generated fields like id and timestamps
    return db_task

def get_task(db: Session, task_id: int) -> Task | None:
    """
    Retrieves a single task by its unique database ID.
    """
    return db.query(Task).filter(Task.id == task_id).first()

def get_user_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list[Task]:
    """
    Retrieves a paginated list of tasks created by a specific user.
    """
    return db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()

def update_task_status(db: Session, task_id: int, status: str, result: str | None = None) -> Task | None:
    """
    Updates the execution status and result payload of a task.
    This is called by background workers when tasks start, finish, or fail.
    """
    db_task = get_task(db, task_id)
    if db_task:
        db_task.status = status
        if result is not None:
            db_task.result = result
        db.commit()
        db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_update: TaskUpdate) -> Task | None:
    """
    Updates a task's title and description.
    """
    db_task = get_task(db, task_id)
    if db_task:
        if task_update.title is not None:
            db_task.title = task_update.title
        if task_update.description is not None:
            db_task.description = task_update.description
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) -> bool:
    """
    Deletes a task from the database.
    """
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False





