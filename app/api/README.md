# API Endpoints & Routing Layer (`app/api/`)

This directory contains endpoint routes configured using FastAPI's `APIRouter`. 

## Key Concept: Decoupled Routing vs. Django ViewSets & `urls.py`
* **Django REST Framework (DRF):** Routers automatically bind URL endpoints to ViewSets. Standard parameters like requests are passed implicitly.
* **FastAPI:** Paths and HTTP methods are defined directly on route handlers via decorators (e.g. `@router.post("/")`). Inputs, parameters, and dependencies are declared explicitly as function arguments.

## Understanding the Subdirectories & Files
* `v1/`: Version 1 API routes:
  * [auth.py](file:///home/jafor/Documents/fastapiandAI/app/api/v1/auth.py): Handles user login, authentication endpoints, and JWT generation.
  * [user.py](file:///home/jafor/Documents/fastapiandAI/app/api/v1/user.py): Defines CRUD operations for users.
  * [task.py](file:///home/jafor/Documents/fastapiandAI/app/api/v1/task.py): Implements CRUD endpoints for background tasks (includes Cache-Aside Redis patterns, Path and Query parameters validation).
  * [upload.py](file:///home/jafor/Documents/fastapiandAI/app/api/v1/upload.py): Implements multi-part file upload endpoints.
  * [ws.py](file:///home/jafor/Documents/fastapiandAI/app/api/v1/ws.py): WebSocket endpoint for real-time task alerts.

## Parameter Handling in FastAPI
FastAPI maps function arguments based on their definitions:
1. **Path Parameters:** Declared in the route URL template (`/{task_id}`). In the function, use the `Path(...)` helper to define range constraints (e.g., ID must be greater than or equal to 1).
2. **Query Parameters:** Declared as primitive types (e.g., `skip: int = 0`) that do NOT match any path parameter name. In the function, use the `Query(...)` helper to apply constraints.
3. **Request Body Parameters:** Declared as Pydantic models (e.g., `task: TaskCreate`). FastAPI automatically parses these from the JSON payload.
4. **Dependency Injection:** Declared using `Depends(dependency_function)` (e.g., `db: Session = Depends(get_db)`). FastAPI resolves dependencies before running the handler.

---

## Detailed Code Walkthrough

### 1. Handling File Uploads (`upload.py`)
```python
@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(..., description="The file payload to upload"),
    current_user: User = Depends(get_current_user)
):
```
* **`file: UploadFile = File(...)`**: Uses `python-multipart` to stream incoming multipart payloads. Unlike loading the whole file into RAM, FastAPI streams chunks into a spooled temporary file on disk.
* **Saving to Disk:** We use `shutil.copyfileobj(file.file, buffer)` to write the bytes efficiently. `file.file` represents the temporary file descriptor. We prefix filenames with `uuid.uuid4().hex` to prevent name collision overrides.
* **Resource Cleanup:** `await file.close()` is placed in a `finally` block to release file descriptors immediately.

### 2. Path vs. Query Validation (`task.py`)
```python
@router.get("/{task_id}", response_model=TaskResponse)
def read_task(
    task_id: int = Path(..., ge=1, description="Task ID")
):
```
* **Path Parameter (`task_id`):** FastAPI matches `{task_id}` in the path to the parameter name. The `Path(..., ge=1)` constraint ensures only positive integers are processed. Any non-conforming request automatically returns a `422 Unprocessable Entity` error before reaching the endpoint code.
```python
@router.get("/", response_model=list[TaskResponse])
def read_tasks(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100)
):
```
* **Query Parameters (`skip`, `limit`):** Because they are not defined in the URL path (`/`), FastAPI parses them from the query string (e.g., `?skip=10&limit=50`). `Query(default=0, ge=0)` defines their validation constraints.

---

## How to Test the API

### Method A: Interactive Swagger Docs
1. Run your server: `uvicorn app.main:app --reload`
2. Open your browser to: `http://127.0.0.1:8000/docs`
3. Click the lock icon (**Authorize**) and login with user credentials (`dev@example.com` / `password123`) to save the JWT cookie.
4. Try out the operations directly (POST, GET, PUT, DELETE) using the interactive interfaces.

### Method B: Terminal Testing with `curl`

1. **Retrieve JWT Access Token**:
```bash
TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=dev@example.com&password=password123" | jq -r '.access_token')
```

2. **Upload a File**:
```bash
echo "FastAPI test data" > test.txt
curl -X POST "http://127.0.0.1:8000/api/v1/upload/" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.txt"
```

3. **Get Pagination List (Query Params)**:
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/tasks/?skip=0&limit=10" \
  -H "Authorization: Bearer $TOKEN"
```

4. **Get Task Details (Path Parameter)**:
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/tasks/1" \
  -H "Authorization: Bearer $TOKEN"
```

