from dataclasses import dataclass
from typing import Any
from omegaconf import MISSING


@dataclass
class EDAConfig:
    input_data_path: str = MISSING
    report_dir: str = MISSING
    report_file_name: str = MISSING
    eda_class: Any = MISSING


@dataclass
class ProfileReportClassParams:
    _target_: str = MISSING
    title: str = MISSING
    explorative: bool = MISSING


@dataclass
class PandasProfilingConfig(EDAConfig):
    eda_class: ProfileReportClassParams = MISSING
