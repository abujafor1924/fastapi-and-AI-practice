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
