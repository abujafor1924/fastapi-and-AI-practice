from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship,Mapped,mapped_column
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True,nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    # Bridge between DB column 'username' and Pydantic field 'name'
    @property
    def name(self) -> str:
        return self.username

    @name.setter
    def name(self, value: str):
        self.username = value

    # Define relationship with Task model
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="owner", cascade="all, delete-orphan")