from fastapi.testclient import TestClient
from schemas.user_schema import UserSchema
from main import app
import pytest

client = TestClient(app)

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "testpassword",
    }

def test_login():
    response = client.post(
        "/auth",
        json=test_user
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data