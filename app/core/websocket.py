import asyncio
import redis.asyncio as aioredis
from fastapi import WebSocket
from app.core.config import settings

# --- WEBSOCKET CONNECTION MANAGER ---
# Keeps track of active client connections.
# Provides helper methods to accept connections, remove them, and broadcast messages.

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Accepts a client connection and registers it."""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Removes a client connection from active list."""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """Sends a text message to all registered active connections."""
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                # Connection might have closed abruptly
                pass

manager = ConnectionManager()


# --- REDIS PUB/SUB BACKGROUND LISTENER ---
# Because FastAPI is asynchronous, we can spin up a background coroutine
# that subscribes to a Redis channel ('task_updates').
# Whenever a Celery worker finishes a job, it publishes a message to Redis.
# This listener catches that message and forwards it via WebSockets.
# This is a highly scalable pattern suitable for production.

async def redis_pubsub_listener():
    """
    Subscribes to the 'task_updates' channel in Redis.
    Listens for events published by Celery workers and broadcasts them to all connected websockets.
    """
    client = aioredis.from_url(settings.REDIS_URL, decode_responses=True)
    pubsub = client.pubsub()
    await pubsub.subscribe("task_updates")
    
    try:
        # listen() returns an async generator yielding messages from Redis
        async for message in pubsub.listen():
            if message and message["type"] == "message":
                data = message.get("data")
                if data:
                    await manager.broadcast(data)
    except asyncio.CancelledError:
        # Clean shutdown when the FastAPI app stops
        await pubsub.unsubscribe("task_updates")
        await client.aclose()
    except Exception as e:
        # In production, log this error
        pass
