import hydra
import pandas as pd
import os

from omegaconf import DictConfig
from src.utils.utils import get_path_from_root
from pathlib import Path


@hydra.main(config_path='../../conf', config_name='config')
def main(cfg: DictConfig) -> None:
    df = pd.read_csv(get_path_from_root(cfg.eda.input_data_path))
    report = hydra.utils.instantiate(cfg.eda.eda_class, df)
    report_dir = get_path_from_root(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    report.to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == '__main__':
    main()
