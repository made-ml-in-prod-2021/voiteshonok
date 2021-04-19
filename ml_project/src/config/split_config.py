from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class SplitConfig:
    name: str = MISSING


@dataclass
class SimpleSplitConfig(SplitConfig):
    test_size: float = MISSING
    random_state: int = MISSING
