# --- BACKGROUND TASK WORKFLOW TESTS ---

def test_create_task_unauthorized(client):
    """
    Verifies that requests without a valid Bearer token are rejected with 401 Unauthorized.
    """
    response = client.post("/api/v1/tasks/", json={"title": "Test Task"})
    assert response.status_code == 401


def test_create_task_and_worker_execution(client):
    """
    Verifies the complete task pipeline:
    1. Authenticates user and sends task payload.
    2. Celery runs task in eager mode (immediately and synchronously).
    3. The response lists the task status as 'completed' with the return result.
    4. Confirms the task is returned in the tasks listing.
    """
    # 1. Register & Login
    client.post(
        "/api/v1/users/",
        json={"name": "taskuser", "email": "tasks@example.com", "password": "password123"}
    )
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "tasks@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. POST Task
    task_payload = {
        "title": "Data Crunching Work",
        "description": "Aggregating metrics for report"
    }
    response = client.post("/api/v1/tasks/", json=task_payload, headers=headers)
    assert response.status_code == 201
    
    task_data = response.json()
    assert task_data["title"] == task_payload["title"]
    assert task_data["description"] == task_payload["description"]
    
    # Because Celery is run in eager mode for tests, the background task completes
    # BEFORE the API request returns! This allows us to check the final state.
    assert task_data["status"] == "completed"
    assert "Output matrix calculated successfully" in task_data["result"]
    assert "id" in task_data

    # 3. GET Tasks (checks cache setting & reading)
    list_response = client.get("/api/v1/tasks/", headers=headers)
    assert list_response.status_code == 200
    tasks_list = list_response.json()
    assert len(tasks_list) >= 1
    assert tasks_list[0]["title"] == task_payload["title"]
