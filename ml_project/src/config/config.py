from dataclasses import dataclass
from .main_config import MainConfig
from .eda_config import EDAConfig
from .split_config import SplitConfig
from .transformer_config import TransformerConfig
from omegaconf import MISSING


@dataclass
class Config:
    main: MainConfig = MISSING
    eda: EDAConfig = MISSING
    split: SplitConfig = MISSING
    transformer: TransformerConfig = MISSING
