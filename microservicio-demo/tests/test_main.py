from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    response = client.get("/health")
    assert response.json() == {"status": "healthy"}

def test_saludo():
    response = client.get("/saludo/Ana")
    assert "Ana" in response.json()["mensaje"]

def test_suma():
    response = client.get("/suma/3/4")
    assert response.json()["resultado"] == 7

def test_resta():
    response = client.get("/resta/10/4")
    assert response.status_code == 200
    assert response.json()["resultado"] == 6