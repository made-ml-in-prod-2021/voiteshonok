import click
import os
import pandas as pd
import pickle

from pathlib import Path
from sklearn import preprocessing
from sklearn.base import TransformerMixin
from typing import Tuple, cast


def load_data(
    load_path: Path,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    features_train, features_test = [
        pd.read_csv(Path(load_path, f"{data_name}.csv"))
        for data_name in ["data_train", "data_test"]
    ]
    targets_train, targets_test = [
        pd.read_csv(Path(load_path, f"{data_name}.csv"), squeeze=True, dtype=int)
        for data_name in ["target_train", "target_test"]
    ]
    return features_train, features_test, targets_train, targets_test


def save_data(
    data_path: Path,
    model_path: Path,
    transformer: TransformerMixin,
    features_train_scaled: pd.DataFrame,
    features_test_scaled: pd.DataFrame,
    targets_train: pd.Series,
    targets_test: pd.Series,
) -> None:
    os.makedirs(data_path, exist_ok=True)
    os.makedirs(model_path, exist_ok=True)
    for dataset, name in zip(
        [features_train_scaled, features_test_scaled, targets_train, targets_test],
        ["data_train", "data_test", "target_train", "target_test"],
    ):
        dataset.to_csv(Path(data_path, f"{name}.csv"), index=False)
    with open(Path(model_path, "transformer.pickle"), "wb") as transformer_file:
        pickle.dump(transformer, transformer_file)


@click.command()
@click.option("--load_path", "-l", required=True)
@click.option("--save_path", "-s", required=True)
@click.option("--model_path", "-m", required=True)
def fit_transformer(load_path: str, save_path: str, model_path: str):
    features_train, features_test, targets_train, targets_test = load_data(
        Path(load_path)
    )
    scaler = cast(
        preprocessing.StandardScaler, preprocessing.StandardScaler().fit(features_train)
    )
    features_train_scaled = pd.DataFrame(
        scaler.transform(features_train), columns=features_train.columns
    )
    features_test_scaled = pd.DataFrame(
        scaler.transform(features_test), columns=features_test.columns
    )
    save_data(
        Path(save_path),
        Path(model_path),
        scaler,
        features_train_scaled,
        features_test_scaled,
        targets_train,
        targets_test,
    )


if __name__ == "__main__":
    fit_transformer()
