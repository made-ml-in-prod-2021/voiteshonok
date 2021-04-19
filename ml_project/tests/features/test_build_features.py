import pandas as pd

from src.features import separate_target


def test_separate_target(dataset: pd.DataFrame, target_name: str):
    data_without_target, target = separate_target(dataset, target_name)
    assert len(data_without_target) > 0
    assert len(data_without_target) == len(target)
