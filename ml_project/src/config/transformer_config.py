from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class TransformerConfig:
    use_scaler: bool = MISSING


@dataclass
class RegressionTransformerConfig(TransformerConfig):
    pass
