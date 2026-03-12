
from pydantic import BaseModel
from typing import List

# This defines what data the user sends to our API
class UserInputSchema(BaseModel):
    age: int
    burning: int           # 0 = No, 1 = Yes
    frequent_urge: int
    cloudy_urine: int
    pelvic_pain: int
    fever: int
    blood_in_urine: int
    back_pain: int
    hydration: int         # 0=Low, 1=Moderate, 2=High
    history: int           # 0 = No, 1 = Yes

# This defines what our API sends back
class PredictionResult(BaseModel):
    probability: float
    risk_level: str
    recommendation: str