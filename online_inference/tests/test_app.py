import pytest
import json

from app import app, load_model, HeartDataModel
from fastapi.testclient import TestClient


@pytest.fixture(scope="session", autouse=True)
def initialize_model():
    load_model()


@pytest.fixture()
def test_data():
    data = [HeartDataModel(id=0), HeartDataModel(id=1)]
    return data


def test_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()


def test_predict(test_data):
    with TestClient(app) as client:
        response = client.post(
            "/predict", data=json.dumps([sample.__dict__ for sample in test_data])
        )
        assert response.status_code == 200
        assert len(response.json()) == len(test_data)
        assert response.json()[0]["id"] == 0
        assert response.json()[0]["target"] in [0, 1]
