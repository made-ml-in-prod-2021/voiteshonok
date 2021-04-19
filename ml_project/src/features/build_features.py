import pandas as pd
import logging

from typing import Tuple


logger = logging.getLogger("mlProject.features.build_features")


def separate_target(
    data: pd.DataFrame, target_name: str
) -> Tuple[pd.DataFrame, pd.Series]:
    logger.info("Started separating target")
    target = data[target_name]
    data_without_target = data.drop(target_name, axis=1)
    logger.info("Finished separating target")
    return data_without_target, target
