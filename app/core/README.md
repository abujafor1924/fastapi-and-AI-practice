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
