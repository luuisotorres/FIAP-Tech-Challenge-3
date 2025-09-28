from pydantic import BaseModel
from enum import Enum

class JobEnum(str, Enum):
    admin = "admin."
    blue_collar = "blue-collar"
    entrepreneur = "entrepreneur"
    housemaid = "housemaid"
    management = "management"
    retired = "retired"
    self_employed = "self-employed"
    services = "services"
    student = "student"
    technician = "technician"
    unemployed = "unemployed"
    unknown = "unknown"

class MaritalEnum(str, Enum):
    divorced = "divorced"
    married = "married"
    single = "single"

class EducationEnum(str, Enum):
    primary = "primary"
    secondary = "secondary"
    tertiary = "tertiary"
    unknown = "unknown"

class YesNoEnum(str, Enum):
    yes = "yes"
    no = "no"

class ContactEnum(str, Enum):
    cellular = "cellular"
    telephone = "telephone"
    unknown = "unknown"

class MonthEnum(str, Enum):
    jan = "jan"
    feb = "feb"
    mar = "mar"
    apr = "apr"
    may = "may"
    jun = "jun"
    jul = "jul"
    aug = "aug"
    sep = "sep"
    oct = "oct"
    nov = "nov"
    dec = "dec"

class PoutcomeEnum(str, Enum):
    success = "success"
    failure = "failure"
    other = "other"
    unknown = "unknown"


class MarketingLead(BaseModel):
    age: int
    job: JobEnum
    marital: MaritalEnum
    education: EducationEnum
    default: YesNoEnum
    balance: float
    housing: YesNoEnum
    loan: YesNoEnum
    contact: ContactEnum
    day_of_month: int
    month: MonthEnum
    campaign: int
    pdays: int
    previous: int
    poutcome: PoutcomeEnum

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