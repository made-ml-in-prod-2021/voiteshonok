from dataclasses import dataclass
from .main_config import MainConfig
from .eda_config import EDAConfig
from omegaconf import MISSING


@dataclass
class Config:
    main: MainConfig = MISSING
    eda: EDAConfig = MISSING
