import click
import numpy as np
import os

from pathlib import Path
from sklearn import datasets
from typing import cast


@click.command()
@click.option("--save_path", "-s", required=True)
@click.option("--n_samples", default=100)
@click.option("--n_features", default=10)
def download_data(save_path: str, n_samples: int, n_features: int) -> None:
    features, targets = datasets.make_blobs(
        n_samples=n_samples, n_features=n_features, centers=2
    )
    features = cast(np.ndarray, features)
    targets = cast(np.ndarray, targets)
    os.makedirs(save_path, exist_ok=True)
    np.savetxt(
        fname=Path(save_path, "data.csv"),
        X=features,
        delimiter=",",
        header=",".join(f"feature_{idx}" for idx in range(n_features)),
        comments="",
    )
    np.savetxt(
        fname=Path(save_path, "target.csv"),
        X=targets,
        delimiter=",",
        header="target",
        comments="",
    )


if __name__ == "__main__":
    download_data()
