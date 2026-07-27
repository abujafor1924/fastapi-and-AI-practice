# Advanced FastAPI & AI Learning Practice

This repository showcases a production-ready, highly modular FastAPI architecture. It is built as a step-by-step learning guide mapping FastAPI, SQLAlchemy, and Pydantic concepts directly to Django/Django REST Framework conventions.

## Key Features
1. **JWT Authentication & Password Hashing** (Bcrypt + Python-jose).
2. **Asynchronous Background Jobs** using **Celery** with **Redis** as a broker.
3. **Real-time Broadcast Alerts** using **WebSockets** and Redis Pub/Sub channels.
4. **Data Cache-Aside Pattern** using Redis database client caching.
5. **Static File Serving & Media Uploads** using FastAPI `UploadFile` streams and mounted folders.

---

## Project Structure

```text
├── alembic/                # Database migrations (Django makemigrations equivalent)
├── alembic.ini             # Alembic configuration pointer
├── app/                    # Primary application codebase
│   ├── api/                # API Endpoints (Django views & urls equivalent)
│   │   ├── v1/             # Version 1 Endpoints (auth, users, tasks, uploads, websockets)
│   │   └── README.md       # API routing and parameters guide
│   ├── core/               # Security, configurations, and system clients (settings.py equivalent)
│   │   └── README.md       # Core configs & security guide
│   ├── crud/               # Isolated Database Query Helpers (Django Managers equivalent)
│   │   └── README.md       # Database CRUD operations guide
│   ├── db/                 # Connection engines & session makers configuration
│   │   └── README.md       # DB pool setup guide
│   ├── models/             # SQLAlchemy ORM Models (Django models equivalent)
│   │   └── README.md       # SQL schema definition guide
│   ├── schemas/            # Pydantic validation schemas (DRF serializers equivalent)
│   │   └── README.md       # Input/Output validation contracts guide
│   ├── tasks/              # Celery task definitions (Asynchronous background workers)
│   │   └── README.md       # Asynchronous workers guide
│   ├── dependencies.py     # FastAPI Dependency Injections (Django request middleware context)
│   ├── main.py             # Root entrypoint instantiating the app & mounting services
│   └── README.md           # Main entry and dependencies guide
├── static/                 # Static media hosting folder (Django MEDIA_ROOT equivalent)
│   ├── uploads/            # Uploaded files destination
│   └── README.md           # Static assets routing guide
├── tests/                  # Pytest automated test suites
├── .env                    # System environment variables file
├── requirements.txt        # Package dependencies list
└── README.md               # Root learning guide (this file)
```

---

## Step-by-Step Installation Guide

### 1. Prerequisite Installations
Ensure you have **Python 3.10+**, **PostgreSQL**, and **Redis Server** installed and running on your system.

### 2. Clone the Repository & Navigate In
```bash
git clone https://github.com/abujafor1924/fastapi-and-AI-practice.git
cd fastapi-and-AI-practice
```

### 3. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Create a file named `.env` in the root directory:
```bash
touch .env
```
Add your PostgreSQL database connection URL (e.g.):
```env
DATABASE_URL=postgresql://postgres:123456@localhost:5432/fastapi_db
```
*(Optionally override default configs like `REDIS_URL=redis://localhost:6379/0` and `SECRET_KEY` if needed)*

---

## How to Run the Application

### Step 1: Run Database Migrations
Generate database tables by running Alembic migrations:
```bash
alembic upgrade head
```

### Step 2: Start the FastAPI Server
Launch Uvicorn to run the development server with hot-reload enabled:
```bash
uvicorn app.main:app --reload
```
The server will boot on: **`http://127.0.0.1:8000`**

### Step 3: Run the Celery Worker Process
Open a **new terminal tab**, activate the virtual environment, and boot Celery:
```bash
source venv/bin/activate
celery -A app.core.celery_app worker --loglevel=info
```

---

## How to Test and Interact with the APIs

### 1. Interactive Swagger Documentation
Open your browser to: **`http://127.0.0.1:8000/docs`**
FastAPI automatically parses Pydantic schemas to construct interactive endpoints. You can test registrations, logins, uploads, and CRUD tasks directly from here.

### 2. Run Automated Pytest Suites
To run all automated cache, user, task, and upload verification suites:
```bash
PYTHONPATH=. pytest
```
*(Or specify the virtual environment path explicitly: `PYTHONPATH=. ./venv/bin/pytest`)*
