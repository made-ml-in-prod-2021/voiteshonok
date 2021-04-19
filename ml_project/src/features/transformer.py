import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class HeartDatasetTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, data: pd.DataFrame, target: pd.Series = None):
        return self

    def transform(self, data: pd.DataFrame, target: pd.Series):
        transformed_data = data.copy()
        transformed_data["oldpeak_zero"] = (transformed_data["oldpeak"] == 0).astype(
            int
        )
        return transformed_data, target
