import pandas as pd
import logging

from sklearn.model_selection import train_test_split
from src.config import SimpleSplitConfig
from typing import Tuple


logger = logging.getLogger("mlProject.data.make_dataset")


def read_data(path: str) -> pd.DataFrame:
    logger.info(f"Started reading data from {path}")
    data = pd.read_csv(path)
    logger.info("Finished reading data")
    return data


def split_train_val_data(
    data: pd.DataFrame, split_config: SimpleSplitConfig
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    logger.info("Started splitting data")
    train_data, val_data = train_test_split(
        data, test_size=split_config.test_size, random_state=split_config.random_state
    )
    logger.info("Finished splitting data")
    return train_data, val_data
