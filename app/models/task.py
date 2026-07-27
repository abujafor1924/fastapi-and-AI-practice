from datetime import datetime, timezone
import datetime as dt
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    
    # Task state: 'queued' -> 'processing' -> 'completed' or 'failed'
    status: Mapped[str] = mapped_column(String(20), default="queued", nullable=False)
    
    # Stores output result or error trace
    result: Mapped[str | None] = mapped_column(String, nullable=True)
    
    # Foreign key link to users table
    user_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=lambda: dt.datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: dt.datetime.now(timezone.utc),
        onupdate=lambda: dt.datetime.now(timezone.utc)
    )

    # Establish ORM relationship back to User
    owner: Mapped["User"] = relationship("User", back_populates="tasks")
