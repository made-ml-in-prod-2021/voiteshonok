import click
import os
import pandas as pd
import pickle

from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from typing import Tuple


def load_data(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(Path(data_path, "data.csv"))


def load_model(model_path: Path) -> Tuple[LogisticRegression, StandardScaler]:
    with open(Path(model_path, "model.pickle"), "rb") as model_file:
        model = pickle.load(model_file)
    with open(Path(model_path, "transformer.pickle"), "rb") as transformer_file:
        transformer = pickle.load(transformer_file)
    return model, transformer


def save_predictions(predictions: pd.Series, predictions_path: Path) -> None:
    os.makedirs(predictions_path, exist_ok=True)
    predictions.to_csv(Path(predictions_path, f"predictions.csv"), index=False)


@click.command()
@click.option("--data_path", "-d", required=True)
@click.option("--model_path", "-m", required=True)
@click.option("--predictions_path", "-p", required=True)
def predict(data_path: str, model_path: str, predictions_path: str):
    dataset = load_data(Path(data_path))
    model, transformer = load_model(Path(model_path))
    predictions = pd.Series(model.predict(transformer.transform(dataset)))
    save_predictions(predictions, Path(predictions_path))


if __name__ == "__main__":
    predict()
