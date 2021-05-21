from src.datamodel.request import HeartDataModel
from typing import Tuple, Union


def check_range(
    value: Union[int, float],
    lower: Union[int, float],
    upper: Union[int, float],
    attr_name: str,
):
    if not (lower <= value <= upper):
        raise ValueError(
            f"{attr_name} should be in range [{lower}, {upper}], got {value}"
        )


def check_binary(value: int, attr_name: str):
    if value not in [0, 1]:
        raise ValueError(f"{attr_name} should be either 0 or 1, got {value}")


def is_sample_valid(sample: HeartDataModel) -> Tuple[bool, str]:
    try:
        check_range(sample.age, 0, 200, "age")
        check_binary(sample.sex, "sex")
        check_range(sample.cp, 0, 3, "cp")
        check_range(sample.trestbps, 50, 500, "trestbps")
        check_range(sample.chol, 50, 1000, "chol")
        check_binary(sample.fbs, "fbs")
        check_range(sample.restecg, 0, 2, "restecg")
        check_range(sample.thalach, 50, 500, "thalach")
        check_binary(sample.exang, "exang")
        check_range(sample.oldpeak, 0, 10, "oldpeak")
        check_range(sample.slope, 0, 2, "slope")
        check_range(sample.ca, 0, 4, "ca")
        check_range(sample.thal, 0, 3, "thal")
        return True, "OK"
    except ValueError as err:
        return False, str(err)
