import pandas as pd

from src.features import HeartDatasetTransformer
from src.features import separate_target
from src.config import TransformerConfig


def test_heart_transformer(
    dataset: pd.DataFrame, transformer_config: TransformerConfig, target_name: str
):
    data, target = separate_target(dataset, target_name)
    transformer = HeartDatasetTransformer(transformer_config).fit(data, target)
    transformed_data, transformed_target = transformer.transform(data, target)
    assert len(transformed_data) == len(data)
    assert len(transformed_target) == len(target)
    assert "oldpeak_zero" in transformed_data
    assert "oldpeak" in transformed_data
    assert (
        transformed_data["oldpeak_zero"].sum()
        == (transformed_data["oldpeak"] == 0).sum()
    )
