# CRUD Database Operations Layer (`app/crud/`)

This directory contains utility functions that interact directly with the PostgreSQL database using SQLAlchemy sessions.

## Key Concept: Explicit Queries vs. Django Managers
* **Django:** Django models have built-in Managers (`User.objects`). Querysets are constructed and evaluated implicitly (e.g. `User.objects.all()`).
* **SQLAlchemy:** Because database access is decoupled from models, you must write helper functions that receive a database `Session` (`db`) as an argument and execute queries explicitly through that session (e.g. `db.query(User).filter(...)`).

## Understanding the Files
* [user.py](file:///home/jafor/Documents/fastapiandAI/app/crud/user.py): Contains functions for creating, retrieving, updating, and deleting user records (hashes passwords on create/update).
* [task.py](file:///home/jafor/Documents/fastapiandAI/app/crud/task.py): Contains database helpers for tasks (e.g., retrieving tasks by owner, task creation, updates, status changes, and deletions).

## Key Differences for Django Developers:
1. **Explicit Session Passing:** Every database transaction requires a session context. The `db: Session` argument is passed from routes where it is injected using FastAPI dependencies.
2. **Transaction Finalization:** Unlike Django which handles transactions implicitly via request/response middleware, in SQLAlchemy you must call `db.commit()` to write changes to PostgreSQL.
3. **Instance Refreshes:** After creating or modifying a database record, use `db.refresh(instance)` to populate database-default values (such as auto-increment IDs, generated timestamps, etc.) back into the Python object.

---

## Detailed Code Walkthrough

### 1. Database Queries (Django vs. SQLAlchemy)
In Django, fetching user tasks looks like:
```python
Task.objects.filter(user_id=user_id)[skip : skip + limit]
```
In SQLAlchemy:
```python
def get_user_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list[Task]:
    return db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()
```
* **`db.query(Task)`**: Initializes a query builder targeted at the `tasks` table.
* **`.filter(...)`**: Corresponds to SQL `WHERE` clause. Notice we use Python comparisons (`Task.user_id == user_id`) instead of Django keyword lookups (`user_id=user_id`).
* **`.offset(skip).limit(limit)`**: Directly compiles to SQL `OFFSET` and `LIMIT` expressions.
* **`.all()`**: Executes the query and returns a list of ORM instances. If retrieving one item, use `.first()` or `.scalar()`.

### 2. DB Modifying Operations (Create / Update / Delete)
```python
def delete_task(db: Session, task_id: int) -> bool:
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
```
* **`db.delete(db_task)`**: Tells the database session to mark the object for removal.
* **`db.commit()`**: Flushes pending changes and runs transaction finalization (`COMMIT`) in PostgreSQL. The row is now permanently deleted.
* **Refreshes:** For creations (`db.add()`), calling `db.refresh(db_task)` sends a quick `SELECT` query to reload server-side database generation values (like serial `id` and auto-generated `created_at` timestamps).

