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
