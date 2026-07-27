# Database Configurations & Session Setup (`app/db/`)

This directory is responsible for setting up the database connection pool, engine, and session makers.

## Key Concept: Connection Pools vs. Django database settings
* **Django:** Databases are configured in `settings.py`. Django manages connection pooling implicitly (with tools like `CONN_MAX_AGE` or pgBouncer).
* **SQLAlchemy:** Connection pooling, dialect compilers, and sessions are configured explicitly using `create_engine` and `sessionmaker`.

## Understanding the Files
* [database.py](file:///home/jafor/Documents/fastapiandAI/app/db/database.py): Exports the `Base` declarative class. All SQLAlchemy models inherit from this `Base` class so they are mapped to the database metadata.
* [session.py](file:///home/jafor/Documents/fastapiandAI/app/db/session.py): Configures the engine via the database URL, creates the `SessionLocal` class which is a factory for database sessions.

## How it works under the hood:
1. **Engine Creation (`create_engine`):** Connects to the database driver and handles low-level pooling.
2. **Session Factory (`sessionmaker`):** Spawns local database session contexts. Setting `autocommit=False` ensures that modifications are wrapped in explicit database transactions that must be manually committed.
3. **Session Lifecycle:** The database session is injected into request handlers via the `get_db` dependency. When the HTTP request starts, a session is initialized, and when the request finishes, the session is cleanly closed.
