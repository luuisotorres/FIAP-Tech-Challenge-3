from pydantic import BaseModel


class Observation(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: float
    housing: str
    loan: str
    contact: str
    day_of_month: int
    month: str
    campaign: int
    pdays: int
    previous: int
    poutcome: str

    class Config:
        json_schema_extra = {
            "example": {
                "age": 64,
                "job": "retired",
                "marital": "divorced",
                "education": "primary",
                "default": "no",
                "balance": 109,
                "housing": "no",
                "loan": "no",
                "contact": "cellular",
                "day_of_month": 23,
                "month": "jun",
                "campaign": 1,
                "pdays": 225,
                "previous": 2,
                "poutcome": "success",
            }
        }