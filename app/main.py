import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
# Import models to ensure they are registered on Base before routers use them
from app import models
from app.api.v1.user import router as user_router
from app.api.v1.auth import router as auth_router
from app.api.v1.task import router as task_router
from app.api.v1.ws import router as ws_router
from app.api.v1.upload import router as upload_router
from app.core.websocket import redis_pubsub_listener
from fastapi.staticfiles import StaticFiles
import os

# --- MODERN FASTAPI LIFESPAN ---
# The lifespan context manager replaces old @app.on_event("startup"/"shutdown").
# It allows us to manage resources (like starting background tasks and closing DB pools)
# during the server startup and shutdown lifecycle.

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Launch the Redis Pub/Sub subscriber coroutine in the background
    pubsub_task = asyncio.create_task(redis_pubsub_listener())
    yield
    # Shutdown: Cancel the subscriber task and await its completion to clean up Redis client
    pubsub_task.cancel()
    try:
        await pubsub_task
    except asyncio.CancelledError:
        pass


app = FastAPI(
    title="FastAPI Advanced Learning App",
    description=(
        "An advanced, production-ready FastAPI application showcasing:\n"
        "1. JWT Authentication & Password Hashing with Bcrypt\n"
        "2. Background Jobs with Celery & Redis\n"
        "3. Real-time Pub/Sub Notifications with WebSockets & Redis\n"
        "4. Cache-Aside Pattern with Redis"
    ),
    version="0.2.0",
    lifespan=lifespan
)

# Register routers under the '/api/v1' version prefix
# Note: user_router already has prefix='/users' inside app/api/v1/user.py,
# so mounting with prefix='/api/v1' exposes endpoints at '/api/v1/users/'
app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")
app.include_router(task_router, prefix="/api/v1")
app.include_router(ws_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")

# Mount the static directory to serve static assets and uploaded files.
# In Django: You define `MEDIA_URL = '/media/'` and `MEDIA_ROOT` settings, and then append it to `urlpatterns`.
# In FastAPI: You explicitly instantiate and mount a StaticFiles instance at a specific path prefix.
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Advanced FastAPI App! Go to /docs for Swagger API documentation."
    }