import time
import json
import redis
from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.crud.task import update_task_status
from app.core.config import settings

# Connect to Redis to publish status messages to our Pub/Sub channel
redis_client = redis.Redis.from_url(settings.REDIS_URL)

@celery_app.task(name="app.tasks.background_tasks.process_heavy_task")
def process_heavy_task(task_id: int):
    """
    Asynchronous Celery task representing a long-running computation.
    - Updates DB status to 'processing' and broadcasts to Redis Pub/Sub.
    - Performs simulated work (sleeping for 5 seconds).
    - Updates DB status to 'completed' (or 'failed' on error) and broadcasts the final outcome.
    """
    db = SessionLocal()
    try:
        # 1. Update task to 'processing' in DB
        update_task_status(db, task_id=task_id, status="processing")
        
        # 2. Publish starting message to Redis Pub/Sub
        redis_client.publish(
            "task_updates",
            json.dumps({
                "task_id": task_id,
                "status": "processing",
                "message": "Task started processing in Celery worker."
            })
        )
        
        # 3. Simulate heavy workload (e.g. data processing or model execution)
        time.sleep(5)
        
        # 4. Save results and update status to 'completed' in DB
        result_content = "Computation finished. Output matrix calculated successfully."
        update_task_status(db, task_id=task_id, status="completed", result=result_content)
        
        # 5. Publish completion message
        redis_client.publish(
            "task_updates",
            json.dumps({
                "task_id": task_id,
                "status": "completed",
                "result": result_content
            })
        )
        
    except Exception as exc:
        # Handle failure cases
        error_msg = f"Task execution failed: {str(exc)}"
        update_task_status(db, task_id=task_id, status="failed", result=error_msg)
        
        redis_client.publish(
            "task_updates",
            json.dumps({
                "task_id": task_id,
                "status": "failed",
                "result": error_msg
            })
        )
        raise exc
    finally:
        db.close()
