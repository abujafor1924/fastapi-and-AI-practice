from app.crud.user import get_user_by_email
from app.core.security import verify_password

# --- USER & AUTHENTICATION TESTS ---

def test_create_user(client, db):
    """
    Test registering a new user.
    Verifies that the API returns 201 Created and that the password is encrypted in the DB.
    """
    payload = {
        "name": "developer",
        "email": "dev@example.com",
        "password": "supersecurepassword123"
    }
    
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["email"] == payload["email"]
    assert data["name"] == payload["name"]
    assert "id" in data
    
    # Query database directly to verify password encryption
    db_user = get_user_by_email(db, email=payload["email"])
    assert db_user is not None
    assert db_user.hashed_password != payload["password"]  # Must NOT be plaintext
    assert verify_password(payload["password"], db_user.hashed_password)  # Must match hash


def test_user_login(client):
    """
    Test user authentication (login).
    Verifies token payload structure and handles incorrect password.
    """
    # 1. Register a test user
    client.post(
        "/api/v1/users/",
        json={"name": "tester", "email": "test@example.com", "password": "password123"}
    )
    
    # 2. Login with wrong password (expect 401)
    wrong_login = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "wrongpassword"}
    )
    assert wrong_login.status_code == 401
    
    # 3. Login with correct credentials (expect 200 and access token)
    correct_login = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "password123"}
    )
    assert correct_login.status_code == 200
    token_data = correct_login.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
