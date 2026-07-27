import io

def test_upload_file_unauthorized(client):
    """
    Verifies that file uploads are blocked for non-authenticated requests.
    """
    file_payload = {"file": ("test.txt", io.BytesIO(b"Hello World"), "text/plain")}
    response = client.post("/api/v1/upload/", files=file_payload)
    assert response.status_code == 401


def test_upload_file_success(client):
    """
    Verifies successful file upload, parsing response schema, and accessing static file directly.
    """
    # 1. Register & Login User
    client.post(
        "/api/v1/users/",
        json={"name": "uploader", "email": "uploader@example.com", "password": "password123"}
    )
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "uploader@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Upload File
    file_content = b"FastAPI file upload content data."
    file_payload = {"file": ("demo_file.txt", io.BytesIO(file_content), "text/plain")}
    
    upload_response = client.post("/api/v1/upload/", files=file_payload, headers=headers)
    assert upload_response.status_code == 201
    
    data = upload_response.json()
    assert "filename" in data
    assert data["content_type"] == "text/plain"
    assert data["size"] == len(file_content)
    assert "url" in data
    
    # 3. Retrieve file from static route
    static_url = data["url"]
    static_response = client.get(static_url)
    assert static_response.status_code == 200
    assert static_response.content == file_content
