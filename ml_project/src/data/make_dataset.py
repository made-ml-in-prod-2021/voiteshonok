import pandas as pd
import logging


logger = logging.getLogger("mlProject.data.make_dataset")


def read_data(path: str) -> pd.DataFrame:
    logger.info(f"Started reading data from {path}")
    data = pd.read_csv(path)
    logger.info(f"Finished reading data")
    return data
