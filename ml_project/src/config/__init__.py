from hydra.core.config_store import ConfigStore
from .config import Config
from .main_config import MainConfig, SaveModelConfig
from .eda_config import PandasProfilingConfig
from .split_config import SimpleSplitConfig
from .transformer_config import TransformerConfig, RegressionTransformerConfig
from .model_config import LogisticRegressionConfig, RandomForestConfig


__all__ = ["Config", "SimpleSplitConfig", "TransformerConfig", "SaveModelConfig"]


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="main", name="main", node=MainConfig)
cs.store(group="eda", name="pd_profiling", node=PandasProfilingConfig)
cs.store(group="split", name="simple_split", node=SimpleSplitConfig)
cs.store(
    group="transformer", name="regression_transformer", node=RegressionTransformerConfig
)
cs.store(group="model", name="logistic_regression", node=LogisticRegressionConfig)
cs.store(group="model", name="random_forest", node=RandomForestConfig)
