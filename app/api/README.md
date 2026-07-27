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
