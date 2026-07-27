from celery import Celery
from app.core.config import settings

# --- CELERY APPLICATION CONFIGURATION ---
# Celery is an asynchronous task queue based on distributed message passing.
# - Message Broker (Redis): Where Celery stores queued jobs before workers pick them up.
# - Result Backend (Redis): Where Celery saves the status and return values of completed jobs.

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

# Configure Celery parameters
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    # task_track_started allows checking if a task is currently executing (status STARTED)
    task_track_started=True,
)

# Auto-discover task functions inside 'app/tasks/' directory.
# The worker will scan app.tasks.background_tasks for tasks decorated with @celery_app.task
celery_app.autodiscover_tasks(["app.tasks"], force=True)
