from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Prepod"}


def test_read_predict_positive():
    response = client.post("/answer/", json={"text": "good"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data[0]["label"] == "positive"
