import pandas as pd


def predict(model: dict, data: pd.DataFrame) -> pd.Series:
    transformer = model["transformer"]
    classifier = model["classifier"]
    transformed_data, _ = transformer.transform(data)
    return pd.Series(classifier.predict(transformed_data))
