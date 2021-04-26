import os
import yaml

from src.model.train_pipeline import train_pipeline
from src.config import Config


def test_train_pipeline(train_config: Config):
    expected_model_path = os.path.join(
        train_config.main.save_model.model_dir,
        train_config.main.save_model.model_weights_file_name,
    )
    expected_experiment_weights_path = os.path.join(
        train_config.main.track.experiment_data_dir,
        train_config.main.track.experiment_dir_name_format,
        train_config.main.track.model_weights_file_name,
    )
    expected_experiment_metrics_path = os.path.join(
        train_config.main.track.experiment_data_dir,
        train_config.main.track.experiment_dir_name_format,
        train_config.main.track.metrics_file_name,
    )
    expected_experiment_config_path = os.path.join(
        train_config.main.track.experiment_data_dir,
        train_config.main.track.experiment_dir_name_format,
        train_config.main.track.config_file_name,
    )
    train_pipeline(train_config)
    for path in [
        expected_model_path,
        expected_experiment_weights_path,
        expected_experiment_metrics_path,
        expected_experiment_config_path,
    ]:
        assert os.path.exists(path)
    with open(expected_experiment_metrics_path, "r") as metrics_file:
        metrics = yaml.load(metrics_file, Loader=yaml.FullLoader)
        assert metrics["accuracy"] > 0
