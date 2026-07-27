# Background Tasks & Workers Layer (`app/tasks/`)

This directory contains Celery task definitions designed to run asynchronous background processes.

## Key Concept: Asynchronous Offloading
For long-running processes (e.g. data reporting, email dispatches, file parsing), running them directly in the request-response thread blocks the server and increases response times. Asynchronous offloading sends tasks to Celery via a broker (Redis) to run asynchronously.

## Understanding the Files
* [background_tasks.py](file:///home/jafor/Documents/fastapiandAI/app/tasks/background_tasks.py): Defines the `@celery_app.task` decorator for the `process_heavy_task` worker.
  - Updates the task's execution status in the PostgreSQL database.
  - Simulates work (sleeping for 5 seconds).
  - Publishes updates to a Redis Pub/Sub channel (`task_updates`) when processing starts and completes.

## Workflow Mechanics:
1. **API Trigger:** The route handler creates a task record in PostgreSQL with a `"queued"` status, then dispatches the task message using `process_heavy_task.delay(db_task.id)`.
2. **Celery Worker Execution:** The Celery worker picks up the message from the Redis queue. It opens its own database session (`SessionLocal()`), updates the task status to `"processing"`, executes the heavy computation, updates the database status to `"completed"` or `"failed"`, and publishes notifications.
3. **Websocket Broadcasting:** The asynchronous Redis Pub/Sub listener running inside FastAPI catches the published event and forwards it to all active WebSockets to alert users in real time.

---

## Detailed Code Walkthrough

### 1. Declaring Background Tasks
```python
@celery_app.task(name="app.tasks.background_tasks.process_heavy_task")
def process_heavy_task(task_id: int):
```
* **`celery_app.task(...)`**: Registers the python function as a Celery task template.
* **Worker Execution Scope:** The worker process runs in a completely separate OS process or even a different server. It does not share memory with FastAPI. Therefore, we pass simple arguments (like the database `task_id` integer) instead of active SQLAlchemy object instances.

### 2. Session Management Inside Workers
```python
db = SessionLocal()
try:
    update_task_status(db, task_id=task_id, status="processing")
    # ... execute work ...
    db.close()
```
* Because Celery runs outside the FastAPI request-response lifecycle, FastAPI's `get_db` dependency injection is not available. The worker must explicitly instantiate the connection pool database session using `SessionLocal()`, execute transactions, and wrap connection closure inside a `finally` block to prevent connection leaks.

---

## How to Run the Celery Worker (Step-by-Step)

To run the background workers, make sure Redis is running, and launch the Celery console in your terminal:

1. **Activate the Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Launch the Celery Worker Process:**
   ```bash
   celery -A app.core.celery_app worker --loglevel=info
   ```
   * **`-A app.core.celery_app`**: Tells Celery where the instantiated Celery application object resides.
   * **`worker`**: Starts the worker thread loop.
   * **`--loglevel=info`**: Enforces descriptive logs printing task dispatches and status results in real time.

