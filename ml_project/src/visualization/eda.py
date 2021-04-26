import hydra
import os
import logging.config

from src.config import Config
from src.utils import get_path_from_root
from src.data import read_data
from pathlib import Path
from omegaconf import OmegaConf


logging.config.fileConfig("conf/logging.conf")
logger = logging.getLogger("mlProject.visualization.eda")


@hydra.main(config_path="../../conf", config_name="config")
def main(cfg: Config) -> None:
    logger.info("Started visualization.eda")
    logger.debug(f"App config: \n{OmegaConf.to_yaml(cfg)}")
    data = read_data(get_path_from_root(cfg.eda.input_data_path))
    report = hydra.utils.instantiate(cfg.eda.eda_class, data)
    logger.info("Report is ready, writing to file")
    report_dir = get_path_from_root(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    report.to_file(os.path.join(report_dir, cfg.eda.report_file_name))
    logger.info("Finished visualization.eda")


if __name__ == "__main__":
    main()
