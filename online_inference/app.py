import logging
import os
import pandas as pd
import pickle
import uvicorn

from fastapi import FastAPI, HTTPException
from sklearn.linear_model import LogisticRegression

from src.datamodel.request import HeartDataModel
from src.datamodel.response import HeartResponse
from src.features import HeartDatasetTransformer
from src.utils import is_sample_valid
from typing import List, Optional

logger = logging.getLogger(__name__)
transformer: Optional[HeartDatasetTransformer] = None
classifier: Optional[LogisticRegression] = None


app = FastAPI()


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
    try:
        model = load_object(model_path)
    except FileNotFoundError as err:
        logger.error(err)
        return
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
    if not health():
        logger.error("Model is not loaded")
        raise HTTPException(
            status_code=500, detail=f"Cannot make a prediction: model is not available"
        )
    for sample in request:
        valid, message = is_sample_valid(sample)
        if not valid:
            raise HTTPException(
                status_code=400, detail=f"For sample id={sample.id}: {message}"
            )
    return make_predictions(request, transformer, classifier)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
