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

---

## Detailed Code Walkthrough

### 1. Declaring Fields (Django vs. SQLAlchemy)
In Django, fields are instantiated classes:
```python
username = models.CharField(max_length=50, unique=True)
```
In modern SQLAlchemy 2.0, we use **Type Annotations** (`Mapped[type]`) and `mapped_column()`:
```python
username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
```
* **`Mapped[str]`**: A Type Hint indicating this attribute maps to a database column containing string data. It helps IDE code completion and linters know the types.
* **`mapped_column(...)`**: Defines the physical column parameters (type constraints, unique flags, indices) sent to PostgreSQL.

### 2. Defining Relationships (Django vs. SQLAlchemy)
In [user.py](file:///home/jafor/Documents/fastapiandAI/app/models/user.py):
```python
tasks: Mapped[List["Task"]] = relationship("Task", back_populates="owner", cascade="all, delete-orphan")
```
In [task.py](file:///home/jafor/Documents/fastapiandAI/app/models/task.py):
```python
user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
owner: Mapped["User"] = relationship("User", back_populates="tasks")
```
* **`ForeignKey("users.id")`**: Binds the constraint at the database engine level.
* **`relationship(...)`**: Creates an in-memory ORM pointer. When you fetch a task `t`, `t.owner` queries the matching User row. The `back_populates="tasks"` tells SQLAlchemy that modifications to `t.owner` should automatically sync with the list `user.tasks` in memory.
* **`cascade="all, delete-orphan"`**: Behaves exactly like Django's `on_delete=models.CASCADE` and orphan-cleanup flag. When a User is deleted (or a task is removed from the `user.tasks` list), the child Task row is deleted automatically in PostgreSQL.

---

## How to Create and Run Migrations (Step-by-Step)

We use **Alembic** for migrations (the Django `makemigrations` and `migrate` equivalent):

1. **Create a migration file (makemigrations equivalent):**
   ```bash
   alembic revision --autogenerate -m "describe your changes here"
   ```
   * Alembic inspects your models in `app/models/__init__.py`, compares them with active tables in PostgreSQL, and generates python instructions inside `alembic/versions/`.

2. **Apply migrations (migrate equivalent):**
   ```bash
   alembic upgrade head
   ```
   * Executes database DDL queries to align the PostgreSQL table structure with models.

