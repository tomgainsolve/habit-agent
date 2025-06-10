import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    """
    return TestClient(app) 