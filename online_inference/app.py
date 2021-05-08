import logging
import os
import pandas as pd
import pickle
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
from src.features import HeartDatasetTransformer
from typing import List, Optional

logger = logging.getLogger(__name__)
transformer: Optional[HeartDatasetTransformer] = None
classifier: Optional[LogisticRegression] = None


app = FastAPI()


class HeartDataModel(BaseModel):
    id: int = 0
    age: int = 54
    sex: int = 1
    cp: int = 0
    trestbps: int = 130
    chol: int = 245
    fbs: int = 0
    restecg: int = 0
    thalach: int = 150
    exang: int = 0
    oldpeak: int = 0
    slope: int = 0
    ca: int = 0
    thal: int = 0


class HeartResponse(BaseModel):
    id: int
    target: int


def load_object(path: str) -> dict:
    with open(path, "rb") as f:
        return pickle.load(f)


def make_predictions(
    data: List[HeartDataModel],
    transformer: HeartDatasetTransformer,
    classifier: LogisticRegression,
) -> List[HeartResponse]:
    df = pd.DataFrame(sample.__dict__ for sample in data)
    transformed_data, _ = transformer.transform(df.drop("id", axis=1))
    predictions = classifier.predict(transformed_data)
    return [
        HeartResponse(id=id_, target=prediction)
        for id_, prediction in zip(df["id"], predictions)
    ]


@app.on_event("startup")
def load_model():
    model_path = os.getenv("PATH_TO_MODEL", default="model.pickle")
    model = load_object(model_path)
    global transformer, classifier
    transformer = model["transformer"]
    classifier = model["classifier"]


@app.get("/")
def main():
    return "this is an entry point of our predictor"


@app.get("/health")
def health() -> bool:
    return (classifier is not None) and (transformer is not None)


@app.post("/predict", response_model=List[HeartResponse])
def predict(request: List[HeartDataModel]):
    return make_predictions(request, transformer, classifier)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
