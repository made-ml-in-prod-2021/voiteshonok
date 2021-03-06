import pytest
import json

from app import app, load_model
from src.datamodel.request import HeartDataModel
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


def test_wrong_type():
    with TestClient(app) as client:
        sample = HeartDataModel()
        sample.sex = "male"
        response = client.post("/predict", data=json.dumps([sample.__dict__]))
        assert response.status_code == 422
        assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


def test_not_binary_feature():
    with TestClient(app) as client:
        sample = HeartDataModel()
        sample.exang = 2
        response = client.post("/predict", data=json.dumps([sample.__dict__]))
        assert response.status_code == 400
        assert (
            response.json()["detail"]
            == f"For sample id=0: exang should be either 0 or 1, got {sample.exang}"
        )


def test_out_of_range():
    with TestClient(app) as client:
        sample = HeartDataModel()
        sample.chol = 1200
        response = client.post("/predict", data=json.dumps([sample.__dict__]))
        assert response.status_code == 400
        assert (
            response.json()["detail"]
            == f"For sample id=0: chol should be in range [50, 1000], got {sample.chol}"
        )
