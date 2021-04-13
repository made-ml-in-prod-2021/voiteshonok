import hydra
import pandas as pd
import os

from omegaconf import DictConfig
from pandas_profiling import ProfileReport
from src.utils.utils import get_path_from_root
from pathlib import Path


@hydra.main(config_path='../../conf', config_name='config')
def main(cfg: DictConfig) -> None:
    profile = ProfileReport(pd.read_csv(get_path_from_root(cfg.eda.input_data_path)),
                            explorative=True)
    report_dir = get_path_from_root(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    profile.to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == '__main__':
    main()
