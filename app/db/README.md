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

---

## Detailed Code Walkthrough

### 1. Database Engine & Dialect Configuration
```python
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)
```
* **`DATABASE_URL`**: Pointer string (e.g. `postgresql://user:pass@localhost/db`) telling SQLAlchemy which SQL dialect parser (e.g., PostgreSQL via `psycopg2`) to bind.
* **`pool_pre_ping=True`**: Connection liveness check. Before handing a cached DB connection to your session, SQLAlchemy sends a quick query (usually `SELECT 1`) to ensure the DB hasn't terminated it. If dead, it rebuilds a fresh connection automatically. This is standard in highly available systems.

### 2. Session Context Creator (`SessionLocal`)
```python
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```
* **`autocommit=False`**: Prevents automatic transaction finalization. Every write (INSERT/UPDATE/DELETE) initiates a transaction scope. Changes are local to the transaction until you call `db.commit()`. If an error occurs, you run `db.rollback()` to undo modifications, mirroring Django's transactional isolation.
* **`autoflush=False`**: Disables auto-flushing modifications to SQL. When enabled, querying tables flushes pending in-memory creations to SQL first to keep query answers consistent. Setting it to `False` gives the programmer explicit control.
* **`bind=engine`**: Binds database operations compiled inside this Session factory to the specified execution engine.

### 3. Declarative Base
```python
class Base(DeclarativeBase):
    pass
```
* In SQLAlchemy 2.0, inheriting from `DeclarativeBase` sets up registry tracking. Every model inheriting from `Base` registers its columns and relationships automatically onto `Base.metadata`. This metadata dictionary maps Python model classes to physical SQL tables, enabling migrations tools (Alembic) to build change scripts.

