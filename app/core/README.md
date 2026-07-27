# Core Modules & Security Configuration (`app/core/`)

This directory contains core configuration logic, custom settings structures, security primitives, and system-wide utilities like caching.

## Key Concept: Decoupled Settings vs. Django's global `settings.py`
* **Django:** Configuration is centralized inside `settings.py` and accessed globally via `from django.conf import settings`.
* **FastAPI:** Configurations are typically driven by a Pydantic-powered class using `pydantic-settings` to load and validate environment variables dynamically.

## Understanding the Files
* [config.py](file:///home/jafor/Documents/fastapiandAI/app/core/config.py): Employs Pydantic's `BaseSettings` to load environment variables from the `.env` file, enforcing types and validation checks.
* [security.py](file:///home/jafor/Documents/fastapiandAI/app/core/security.py): Handles bcrypt password hashing, verifies credentials, and compiles JSON Web Tokens (JWT) for authentication.
* [celery_app.py](file:///home/jafor/Documents/fastapiandAI/app/core/celery_app.py): Configures Celery workers to connect to the Redis task broker.
* [cache.py](file:///home/jafor/Documents/fastapiandAI/app/core/cache.py): Implements cache wrappers for Redis to support the Cache-Aside pattern.
* [websocket.py](file:///home/jafor/Documents/fastapiandAI/app/core/websocket.py): Handles WebSocket clients connection registration and implements an asynchronous Redis Pub/Sub listener to broadcast real-time task alerts.

## Key Differences for Django Developers:
1. **Pydantic Settings:** `Settings` handles environment parsing automatically. If you define a setting as an integer `PORT: int`, Pydantic automatically casts the environment string `"8000"` to `8000`, raising an initialization error if variables are missing or incorrect.
2. **Explicit JWT Authentication:** Rather than importing custom middleware packages, JWT compilation is written explicitly. Tokens contain expiration payloads and security signatures to validate the client's session.

---

## Detailed Code Walkthrough

### 1. Password Hashing & Authentication (`security.py`)
```python
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```
* **`CryptContext`**: Provided by `passlib`. It wraps the `bcrypt` algorithm, handling salt generation and hashing operations automatically.
* **`verify_password(...)`**: Safely compares input strings against stored hashes using constant-time comparison to prevent timing side-channel attacks.

### 2. JWT Generation & Validation (`security.py`)
```python
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
```
* **Payload Structure:** We pass the user's identifier (email) in the `"sub"` key.
* **Signature compilation:** The `jwt.encode` merges the payload dictionary with the `SECRET_KEY` using HMAC SHA-256 (`HS256`) to issue a tamper-proof cryptographically signed token string.

### 3. WebSocket Pub/Sub Connection Manager (`websocket.py`)
```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
```
* **Connection Lifecycle:** When clients open a WebSocket hand-shake (handled inside `app/api/v1/ws.py`), we accept the stream and add it to `active_connections`.
* **Redis Pub/Sub Listener:**
  ```python
  async def redis_pubsub_listener():
      client = aioredis.from_url(settings.REDIS_URL, decode_responses=True)
      pubsub = client.pubsub()
      await pubsub.subscribe("task_updates")
      async for message in pubsub.listen():
          if message and message["type"] == "message":
              await manager.broadcast(message["data"])
  ```
  This asynchronous listener runs permanently in the background. When a Celery worker completes a task and publishes JSON status updates to the Redis `"task_updates"` channel, this generator wakes up, extracts the message payload, and calls `manager.broadcast()` to relay the update to all active user WebSockets concurrently.

