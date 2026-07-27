import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.database import Base
from app.dependencies import get_db
from app.core.config import settings
from app.core.celery_app import celery_app

# --- TESTING CONFIGURATION (CONFTEST) ---
# Pytest uses conftest.py to share fixtures across multiple test modules.
# - task_always_eager=True: Configures Celery to run tasks synchronously in the same process
#   during tests, avoiding the need to run an external Celery worker.
# - Transaction Rollback: Wraps each test in a database transaction and rolls it back,
#   ensuring no database pollution between tests.

celery_app.conf.update(task_always_eager=True)

# Connect to the Postgres database configured in settings
engine = create_engine(settings.DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import sqlalchemy as sa

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    """Ensure database schema is created once before the entire test suite runs."""
    Base.metadata.create_all(bind=engine)
    yield
    # Clean up tables at the end of the session
    with engine.connect() as connection:
        connection.execute(sa.text("DROP TABLE IF EXISTS tasks CASCADE;"))
        connection.execute(sa.text("DROP TABLE IF EXISTS users CASCADE;"))
        connection.commit()

@pytest.fixture
def db():
    """
    Creates a new database session.
    Cleans up all table data after each test to maintain test isolation.
    """
    session = TestingSessionLocal()
    
    yield session
    
    session.close()
    
    # Truncate tables to ensure tests run in isolation
    with engine.connect() as connection:
        connection.execute(sa.text("TRUNCATE TABLE tasks, users RESTART IDENTITY CASCADE;"))
        connection.commit()

@pytest.fixture
def client(db):
    """
    Overrides the database dependency to yield our transactional test session.
    Yields a TestClient instance.
    """
    def override_get_db():
        try:
            yield db
        finally:
            pass
            
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
