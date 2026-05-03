from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict():
    response = client.post("/predict", json={
        "product": "ProductoA",
        "base_sales": 1000.0,
        "month": 5
    })
    assert response.status_code == 200
    assert "predicted_sales" in response.json()
    assert "confidence" in response.json()