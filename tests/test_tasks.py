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


def test_update_task_success(client):
    """
    Tests successful title and description update by the task owner.
    """
    # 1. Register & Login
    client.post(
        "/api/v1/users/",
        json={"name": "user1", "email": "user1@example.com", "password": "password123"}
    )
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "user1@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. POST Task
    task_payload = {"title": "Original Title", "description": "Original Description"}
    create_response = client.post("/api/v1/tasks/", json=task_payload, headers=headers)
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # 3. PUT Task (Update)
    update_payload = {"title": "Updated Title", "description": "Updated Description"}
    update_response = client.put(f"/api/v1/tasks/{task_id}", json=update_payload, headers=headers)
    assert update_response.status_code == 200
    
    updated_data = update_response.json()
    assert updated_data["title"] == "Updated Title"
    assert updated_data["description"] == "Updated Description"


def test_update_task_unauthorized_and_not_found(client):
    """
    Verifies that updating a task belonging to another user fails with 404,
    and updating a non-existent task fails with 404.
    """
    # 1. Register & Login User 1
    client.post(
        "/api/v1/users/",
        json={"name": "user1", "email": "user1@example.com", "password": "password123"}
    )
    login_response_1 = client.post(
        "/api/v1/auth/login",
        data={"username": "user1@example.com", "password": "password123"}
    )
    token_1 = login_response_1.json()["access_token"]
    headers_1 = {"Authorization": f"Bearer {token_1}"}

    # 2. Register & Login User 2
    client.post(
        "/api/v1/users/",
        json={"name": "user2", "email": "user2@example.com", "password": "password123"}
    )
    login_response_2 = client.post(
        "/api/v1/auth/login",
        data={"username": "user2@example.com", "password": "password123"}
    )
    token_2 = login_response_2.json()["access_token"]
    headers_2 = {"Authorization": f"Bearer {token_2}"}

    # 3. User 1 creates a task
    create_response = client.post(
        "/api/v1/tasks/",
        json={"title": "User 1 Task"},
        headers=headers_1
    )
    task_id = create_response.json()["id"]

    # 4. User 2 tries to update User 1's task (expect 404)
    update_payload = {"title": "Hacked Title"}
    update_response = client.put(f"/api/v1/tasks/{task_id}", json=update_payload, headers=headers_2)
    assert update_response.status_code == 404

    # 5. User 1 tries to update a non-existent task (expect 404)
    update_response_nonexistent = client.put("/api/v1/tasks/99999", json=update_payload, headers=headers_1)
    assert update_response_nonexistent.status_code == 404


def test_delete_task_success(client):
    """
    Tests successful task deletion by the owner.
    """
    # 1. Register & Login
    client.post(
        "/api/v1/users/",
        json={"name": "user1", "email": "user1@example.com", "password": "password123"}
    )
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "user1@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. POST Task
    create_response = client.post(
        "/api/v1/tasks/",
        json={"title": "To Delete"},
        headers=headers
    )
    task_id = create_response.json()["id"]

    # 3. DELETE Task
    delete_response = client.delete(f"/api/v1/tasks/{task_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Task deleted successfully"}

    # 4. GET Task (expect 404 now)
    get_response = client.get(f"/api/v1/tasks/{task_id}", headers=headers)
    assert get_response.status_code == 404


def test_delete_task_unauthorized_and_not_found(client):
    """
    Verifies that deleting a task belonging to another user fails with 404,
    and deleting a non-existent task fails with 404.
    """
    # 1. Register & Login User 1
    client.post(
        "/api/v1/users/",
        json={"name": "user1", "email": "user1@example.com", "password": "password123"}
    )
    login_response_1 = client.post(
        "/api/v1/auth/login",
        data={"username": "user1@example.com", "password": "password123"}
    )
    token_1 = login_response_1.json()["access_token"]
    headers_1 = {"Authorization": f"Bearer {token_1}"}

    # 2. Register & Login User 2
    client.post(
        "/api/v1/users/",
        json={"name": "user2", "email": "user2@example.com", "password": "password123"}
    )
    login_response_2 = client.post(
        "/api/v1/auth/login",
        data={"username": "user2@example.com", "password": "password123"}
    )
    token_2 = login_response_2.json()["access_token"]
    headers_2 = {"Authorization": f"Bearer {token_2}"}

    # 3. User 1 creates a task
    create_response = client.post(
        "/api/v1/tasks/",
        json={"title": "User 1 Task"},
        headers=headers_1
    )
    task_id = create_response.json()["id"]

    # 4. User 2 tries to delete User 1's task (expect 404)
    delete_response = client.delete(f"/api/v1/tasks/{task_id}", headers=headers_2)
    assert delete_response.status_code == 404

    # 5. User 1 tries to delete a non-existent task (expect 404)
    delete_response_nonexistent = client.delete("/api/v1/tasks/99999", headers=headers_1)
    assert delete_response_nonexistent.status_code == 404

