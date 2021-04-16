import pytest
import os


@pytest.fixture()
def dataset_path():
    curdir = os.path.dirname(__file__)
    return os.path.join(curdir, "data_sample.zip")


@pytest.fixture()
def target_col():
    return "restecg"
