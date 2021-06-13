import pandas as pd
import pytest

from click.testing import CliRunner
from download import download_data
from pathlib import Path


@pytest.fixture
def n_features() -> int:
    return 5


@pytest.fixture()
def n_samples() -> int:
    return 150


def test_download(n_features: int, n_samples: int) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        save_path = Path("data", "raw")
        result = runner.invoke(
            download_data,
            [
                "--save_path",
                str(save_path),
                "--n_features",
                n_features,
                "--n_samples",
                n_samples,
            ],
        )
        assert result.exit_code == 0
        features_df = pd.read_csv(Path(save_path, "data.csv"))
        assert type(features_df) == pd.DataFrame
        assert features_df.shape == (n_samples, n_features)
        targets_series = pd.read_csv(
            Path(save_path, "target.csv"), squeeze=True, dtype=int
        )
        assert type(targets_series) == pd.Series
        assert targets_series.shape == (n_samples,)
        assert targets_series.dtype == int
        assert targets_series.min() >= 0
        assert targets_series.max() <= 1
