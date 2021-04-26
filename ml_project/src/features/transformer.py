import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from src.config import TransformerConfig


class HeartDatasetTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, cfg: TransformerConfig):
        self.cfg = cfg
        self.scaler = StandardScaler()

    def fit(self, data: pd.DataFrame, target: pd.Series = None):
        if self.cfg.use_scaler:
            self.scaler.fit(data)
        return self

    def transform(self, data: pd.DataFrame, target: pd.Series = None):
        transformed_data = data.copy()
        transformed_data["oldpeak_zero"] = (transformed_data["oldpeak"] == 0).astype(
            int
        )
        if self.cfg.use_scaler:
            self.scaler.transform(data)
        return transformed_data, target
