from hydra.core.config_store import ConfigStore
from .config import Config
from .main_config import MainConfig
from .eda_config import PandasProfilingConfig
from .split_config import SimpleSplitConfig


__all__ = ["Config", "SimpleSplitConfig"]


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="main", name="main", node=MainConfig)
cs.store(group="eda", name="pd_profiling", node=PandasProfilingConfig)
cs.store(group="split", name="simple_split", node=SimpleSplitConfig)
