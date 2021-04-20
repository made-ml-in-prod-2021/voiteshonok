import pytest
import os
import pandas as pd
import omegaconf

from tests.utils import create_fake_dataset
from src.config import SimpleSplitConfig, TransformerConfig, Config
from hydra.experimental import compose, initialize
from src.data import read_data
from typing import cast


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


@pytest.fixture()
def target_name() -> str:
    return "target"


@pytest.fixture()
def transformer_config() -> TransformerConfig:
    return TransformerConfig(use_scaler=True)


@pytest.fixture()
def model_dir() -> str:
    return os.path.join(os.path.dirname(__file__), "model_test_dir")


@pytest.fixture()
def train_config(model_dir, dataset_path) -> Config:
    initialize(config_path="../conf", job_name="test_app")
    cfg = compose(config_name="config")
    cfg = cast(Config, cfg)
    cfg.main.track.experiment_dir_name_format = "test_experiment"
    cfg.main.track.experiment_data_dir = model_dir
    cfg.main.save_model.model_dir = model_dir
    cfg.main.save_model.overwrite_main_model = True
    cfg.main.track.track_experiment = True
    cfg.main.track.save_model_weights = True
    cfg.main.input_data_path = dataset_path
    print(cfg)
    return cfg
