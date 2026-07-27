# Core Application Entry & Dependencies (`app/`)

This directory contains the root initialization module and application-wide dependencies.

---

## Detailed Walkthrough: `app/main.py`

[main.py](file:///home/jafor/Documents/fastapiandAI/app/main.py) is the entry point of the FastAPI application. It instantiates the app, handles startup/shutdown events, configures routers, and mounts static files.

### 1. Lifespan Manager (Startup & Shutdown)
In Django, you use signals (`startup`, `shutdown`) or custom AppConfig `ready()` methods. FastAPI uses a modern `lifespan` context manager:
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Phase
    pubsub_task = asyncio.create_task(redis_pubsub_listener())
    yield
    # Shutdown Phase
    pubsub_task.cancel()
    try:
        await pubsub_task
    except asyncio.CancelledError:
        pass
```
* **Startup:** Spawns `redis_pubsub_listener()` as a concurrent background task to listen for Celery notifications.
* **`yield`**: Hands control over to FastAPI to start accepting HTTP requests.
* **Shutdown:** Triggered when the server is stopped (e.g. `Ctrl+C`). It cancels the subscriber task cleanly and releases connections.

### 2. FastAPI Application & Routers Mount
```python
app = FastAPI(title="...", version="...", lifespan=lifespan)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")
# ...
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
```
* Registers Version 1 API routers under the prefix `/api/v1`.
* Mounts the static directory to serve file uploads.

---

## Detailed Walkthrough: `app/dependencies.py`

[dependencies.py](file:///home/jafor/Documents/fastapiandAI/app/dependencies.py) implements FastAPI's **Dependency Injection** pattern, replacing typical Django Middleware contexts (e.g., retrieving `request.user` or managing database transactions).

### 1. Database Connection Generator (`get_db`)
```python
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
* **How it works:** When a route calls `Depends(get_db)`, FastAPI runs the code up to `yield db`, providing an active database transaction session to the router. Once the HTTP response is dispatched, the `finally` block is executed, closing the session to prevent database pool exhaustion.

### 2. Authorization Security Scheme (`oauth2_scheme`)
```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
```
* **How it works:** FastAPI automatically inspects incoming request headers looking for the standard header: `Authorization: Bearer <JWT_TOKEN>`. The `tokenUrl` tells Swagger UI where to send credentials when clicking the "Authorize" button.

### 3. User Authentication (`get_current_user`)
```python
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
```
* **Depends Chain:** `get_current_user` depends on both the `oauth2_scheme` (token string) and `get_db` (database session).
* **Execution Flow:**
  1. Decodes the JWT token payload. If expired or corrupted, raises `401 Unauthorized`.
  2. Extracts the email subject (`sub`) key.
  3. Queries PostgreSQL for the user. If the user record no longer exists, raises `401 Unauthorized`.
  4. Returns the verified `User` instance, which is injected directly into protected endpoint functions.
