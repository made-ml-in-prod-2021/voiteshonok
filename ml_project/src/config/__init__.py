from hydra.core.config_store import ConfigStore
from .config import Config
from .main_config import MainConfig
from .eda_config import PandasProfilingConfig
from .split_config import SimpleSplitConfig
from .transformer_config import TransformerConfig, RegressionTransformerConfig


__all__ = ["Config", "SimpleSplitConfig", "TransformerConfig"]


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="main", name="main", node=MainConfig)
cs.store(group="eda", name="pd_profiling", node=PandasProfilingConfig)
cs.store(group="split", name="simple_split", node=SimpleSplitConfig)
cs.store(
    group="transformer", name="regression_transformer", node=RegressionTransformerConfig
)
