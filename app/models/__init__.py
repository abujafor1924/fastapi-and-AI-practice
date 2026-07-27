from app.db.database import Base
from app.models.user import User
from app.models.task import Task

# Expose models so that they are registered on the Base.metadata
__all__ = ["Base", "User", "Task"]
