from pydantic import BaseModel


class HeartDataModel(BaseModel):
    id: int = 0
    age: int = 54
    sex: int = 1
    cp: int = 0
    trestbps: int = 130
    chol: int = 245
    fbs: int = 0
    restecg: int = 0
    thalach: int = 150
    exang: int = 0
    oldpeak: float = 0
    slope: int = 0
    ca: int = 0
    thal: int = 0
