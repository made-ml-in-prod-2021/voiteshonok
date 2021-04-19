from src.data import read_data, split_train_val_data
from src.config import SimpleSplitConfig


def test_read_data(dataset_path: str, target_col: str):
    data = read_data(dataset_path)
    assert len(data) > 10
    assert target_col in data.keys()


def test_split_train_val_data(dataset_path: str, split_config: SimpleSplitConfig):
    data = read_data(dataset_path)
    train_data, val_data = split_train_val_data(data, split_config)
    assert len(train_data) > 0
    assert len(val_data) > 0
