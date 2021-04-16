import pytest
import os

from tests.utils import create_fake_dataset


@pytest.fixture()
def src_path():
    return "src"


@pytest.fixture()
def tests_path():
    return "tests"


@pytest.fixture()
def dataset_path():
    path = os.path.join(os.path.dirname(__file__), "data_sample.zip")
    data = create_fake_dataset()
    data.to_csv(path, compression="zip")
    return path


@pytest.fixture()
def target_col():
    return "restecg"
