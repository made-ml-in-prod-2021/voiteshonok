import pytest
import os
import pandas as pd

from tests.utils import create_fake_dataset
from src.config import SimpleSplitConfig
from src.data import read_data


@pytest.fixture()
def src_path() -> str:
    return "src"


@pytest.fixture()
def tests_path() -> str:
    return "tests"


@pytest.fixture()
def dataset_path() -> str:
    path = os.path.join(os.path.dirname(__file__), "data_sample.zip")
    data = create_fake_dataset()
    data.to_csv(path, compression="zip")
    return path


@pytest.fixture()
def dataset(dataset_path) -> pd.DataFrame:
    return read_data(dataset_path)


@pytest.fixture()
def target_col() -> str:
    return "restecg"


@pytest.fixture()
def split_config() -> SimpleSplitConfig:
    return SimpleSplitConfig(test_size=0.2, random_state=42)
