import click
import os
import pandas as pd
import pickle

from pathlib import Path
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from typing import cast, Tuple


def load_data(data_path: Path) -> Tuple[pd.DataFrame, pd.Series]:
    return (
        pd.read_csv(Path(data_path, "data_train.csv")),
        pd.read_csv(Path(data_path, "target_train.csv"), squeeze=True, dtype=int),
    )


def save_model(model: BaseEstimator, model_path: Path):
    os.makedirs(model_path, exist_ok=True)
    with open(Path(model_path, "model.pickle"), "wb") as model_file:
        pickle.dump(model, model_file)


@click.command()
@click.option("--data_path", "-d", required=True)
@click.option("--model_path", "-m", required=True)
@click.option("--random_state", "-r", default=42)
def fit_model(data_path: str, model_path: str, random_state: int):
    data_train, target_train = load_data(Path(data_path))
    model = cast(
        LogisticRegression,
        LogisticRegression(random_state=random_state).fit(data_train, target_train),
    )
    save_model(model, Path(model_path))


if __name__ == "__main__":
    fit_model()
