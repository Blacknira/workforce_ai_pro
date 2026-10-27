from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmployeeCreate(BaseModel):
    name: str
    department: str
    job_role: str
    monthly_income: int
    job_satisfaction: int
    years_at_company: int
    over_time: bool = False
    work_life_balance: int

class EmployeeResponse(EmployeeCreate):
    id: int
    class Config:
        from_attributes = True

class PredictionResponse(BaseModel):
    employee_id: int
    risk_score: float
    risk_level: str
    factors: str