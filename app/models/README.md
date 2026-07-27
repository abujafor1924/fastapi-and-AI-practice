# SQLAlchemy Database Models Layer (`app/models/`)

This directory contains SQLAlchemy declarative models representing the database schema.

## Key Concept: Data Mapper vs. Active Record
* **Django:** Django ORM uses the **Active Record** pattern. Your model class defines the table schema, contains validation logic, and carries database-access capability (e.g. `user.save()` or `User.objects.filter()`).
* **SQLAlchemy:** SQLAlchemy uses the **Data Mapper** pattern. Models (classes in this directory) are simple Python objects containing schema structural definitions only. They are completely decoupled from database communication. Database queries and persistence are handled explicitly by the `Session` (in `app/crud/`).

## Understanding the Files
* [user.py](file:///home/jafor/Documents/fastapiandAI/app/models/user.py): Defines the `users` table, password hash fields, and relationships.
* [task.py](file:///home/jafor/Documents/fastapiandAI/app/models/task.py): Defines the `tasks` table, status enums, foreign keys, and timestamps.
* [\_\_init\_\_.py](file:///home/jafor/Documents/fastapiandAI/app/models/__init__.py): Exposes all models to ensure SQLAlchemy's `Base.metadata` registers them before migrations (Alembic) run.

## Key Differences for Django Developers:
1. **Explicit Foreign Keys:** In Django, `ForeignKey("User")` implicitly creates a database field named `user_id` and adds a reverse accessor `user.task_set`. In SQLAlchemy, you must define the physical column `user_id: Mapped[int] = mapped_column(ForeignKey(...))` and the relationship helper `owner: Mapped["User"] = relationship(...)` separately.
2. **Reverse Relationships:** SQLAlchemy requires explicit `relationship("Model", back_populates="field")` on BOTH models to enable bi-directional navigation. In Django, this is generated automatically unless overridden by `related_name`.
3. **No Automatic Database Sync:** Modifications to these files do not sync to the DB automatically. Use `alembic revision --autogenerate` to build migrations (similar to `manage.py makemigrations`) and `alembic upgrade head` to run them (similar to `manage.py migrate`).
