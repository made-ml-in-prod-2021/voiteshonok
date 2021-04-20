from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class TrackConfig:
    track_experiment: bool = MISSING
    experiment_data_dir: str = MISSING
    save_model_weights: bool = MISSING
    metrics_file_name: str = MISSING
    config_file_name: str = MISSING
    model_weights_file_name: str = MISSING
    experiment_dir_name_format: str = MISSING


@dataclass
class SaveModelConfig:
    overwrite_main_model: bool = MISSING
    model_dir: str = MISSING
    model_weights_file_name: str = MISSING


@dataclass
class MainConfig:
    input_data_path: str = MISSING
    eda_dir: str = MISSING
    random_seed: int = MISSING
    target_name: str = MISSING
    track: TrackConfig = MISSING
    save_model: SaveModelConfig = MISSING
