import hydra
import os

from omegaconf import DictConfig
from src.utils.utils import get_path_from_root
from src.data.make_dataset import read_data
from pathlib import Path


@hydra.main(config_path="../../conf", config_name="config")
def main(cfg: DictConfig) -> None:
    data = read_data(get_path_from_root(cfg.eda.input_data_path))
    report = hydra.utils.instantiate(cfg.eda.eda_class, data)
    report_dir = get_path_from_root(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    report.to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == "__main__":
    main()
