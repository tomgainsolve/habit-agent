from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check(client):
    """
    Test the health check endpoint returns correct response.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": "0.1.0"
    } 