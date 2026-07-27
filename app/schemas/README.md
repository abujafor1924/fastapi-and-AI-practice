# Pydantic Validation & Serialization Layer (`app/schemas/`)

This directory contains Pydantic models (referred to as **schemas** in FastAPI) which handle input data validation, parsing, type coercion, and JSON serialization.

## Key Concept: Schemas vs. DRF Serializers
* **Django REST Framework (DRF):** DRF Serializers validate incoming request data, deserialize it into Python types, and serialize Django model queries back into JSON.
* **FastAPI (Pydantic):** Pydantic handles validation, type coercion, and serialization/deserialization. Rather than custom Serializer fields (`serializers.CharField`), you use standard Python type annotations (`str`, `int`, `datetime`) coupled with Pydantic's `Field(...)` helper.

## Understanding the Files
* [user.py](file:///home/jafor/Documents/fastapiandAI/app/schemas/user.py): Defines input models for registration/login and response models showing active users.
* [task.py](file:///home/jafor/Documents/fastapiandAI/app/schemas/task.py): Defines input schema for creation (`TaskCreate`), modification (`TaskUpdate`), and response payloads (`TaskResponse`).

## Key Differences for Django Developers:
1. **Strong Typings:** Pydantic uses pure Python type hints. If you specify `id: int`, Pydantic will cast the string `"123"` to the integer `123` automatically. If casting is impossible (e.g., `"abc"`), it immediately raises validation errors.
2. **Model Compatibility (`from_attributes=True`):** By default, Pydantic only works with dictionary data. Setting `model_config = ConfigDict(from_attributes=True)` enables it to read fields directly from ORM objects (e.g., calling `db_task.title` instead of looking up keys), similar to how DRF's `ModelSerializer` communicates with Django ORMs.
3. **Decoupled Contracts:** Keep request models (e.g., `TaskCreate`) separate from output models (e.g., `TaskResponse`). This prevents API users from injecting server-controlled fields like `status` or `result` during standard resource creations.
