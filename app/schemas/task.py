from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

# --- TASK PYDANTIC SCHEMAS ---
# Pydantic models are used for data validation, serialization, and OpenAPI documentation.
# By separating incoming schemas (like TaskCreate) from database representations (like TaskResponse),
# we prevent clients from injecting internal fields like 'status' or 'result' directly.

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="The title of the background task")
    description: str | None = Field(None, max_length=255, description="An optional detailed description of the task")

class TaskCreate(TaskBase):
    """
    Schema for creating a task. Clients only send the title and description.
    """
    pass

class TaskResponse(TaskBase):
    """
    Schema representing the task response. Exposes the DB status, result, and ownership.
    """
    id: int
    status: str
    result: str | None = None
    user_id: int
    created_at: datetime
    updated_at: datetime

    # Enable SQLAlchemy model compatibility (allows Pydantic to read ORM objects)
    model_config = ConfigDict(from_attributes=True)

class TaskUpdateStatus(BaseModel):
    """
    Used internally or by Celery workers to update a task's status and results.
    """
    status: str
    result: str | None = None
