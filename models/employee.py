from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base
from datetime import datetime

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_code = Column(String(20), unique=True) # EMP001
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    department = Column(String(50), index=True)
    job_role = Column(String(50))
    
    # AI Prediction Features
    monthly_income = Column(Integer, default=50000)
    job_satisfaction = Column(Integer) # 1-4
    work_life_balance = Column(Integer) # 1-4
    years_at_company = Column(Integer, default=1)
    years_in_current_role = Column(Integer, default=1)
    over_time = Column(Boolean, default=False)
    distance_from_home = Column(Integer, default=10)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)