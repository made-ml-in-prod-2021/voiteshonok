import click
import pandas as pd
import pickle

from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from typing import Tuple


def load_data(data_path: Path) -> Tuple[pd.DataFrame, pd.Series]:
    return (
        pd.read_csv(Path(data_path, "data_test.csv")),
        pd.read_csv(Path(data_path, "target_test.csv"), squeeze=True, dtype=int),
    )


def load_model(model_path: Path) -> LogisticRegression:
    with open(Path(model_path, "model.pickle"), "rb") as model_file:
        model = pickle.load(model_file)
    return model


def save_results(report: str, model_path: Path) -> None:
    with open(Path(model_path, "validation_result.txt"), "w") as results_file:
        results_file.write(report)


@click.command()
@click.option("--data_path", "-d", required=True)
@click.option("--model_path", "-m", required=True)
def validate(data_path: str, model_path: str):
    data_test, target_test = load_data(Path(data_path))
    model = load_model(Path(model_path))
    report = classification_report(target_test, model.predict(data_test))
    save_results(report, Path(model_path))


if __name__ == "__main__":
    validate()
