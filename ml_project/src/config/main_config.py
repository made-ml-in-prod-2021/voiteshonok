from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class MainConfig:
    input_data_path: str = MISSING
    eda_dir: str = MISSING
