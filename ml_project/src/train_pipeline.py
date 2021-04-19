import hydra
import logging.config

from omegaconf import OmegaConf
from src.config import Config
from src.data import read_data, split_train_val_data
from src.utils import get_path_from_root


logging.config.fileConfig("conf/logging.conf")
logger = logging.getLogger("mlProject.train_pipeline")


@hydra.main(config_path="../conf", config_name="config")
def main(cfg: Config):
    logger.info("Started train pipeline")
    logger.debug(f"App config: \n{OmegaConf.to_yaml(cfg)}")
    data = read_data(get_path_from_root(cfg.main.input_data_path))
    logger.debug(f"Data shape is {data.shape}")
    if cfg.split.name == "simple_split":
        train_data, val_data = split_train_val_data(data, cfg.split)
    else:
        error_msg = f"Wrong split strategy {cfg.split.name}"
        logger.error(error_msg)
        raise ValueError(error_msg)
    logger.info("Finished train pipeline")


if __name__ == "__main__":
    main()
