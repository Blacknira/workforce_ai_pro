from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from app.database import Base
from datetime import datetime

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    activity_type = Column(String(50)) # LOGIN, TASK_COMPLETED, LEAVE_APPLIED, PERFORMANCE_UPDATE, SALARY_CHANGE
    description = Column(Text)
    old_value = Column(String(100), nullable=True)
    new_value = Column(String(100), nullable=True)
    
    # For Real-Time Monitoring
    ip_address = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Intervention(Base):
    __tablename__ = "interventions"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    prediction_id = Column(Integer, ForeignKey("attrition_predictions.id"))
    
    action_type = Column(String(50)) # COUNSELING, SALARY_REVIEW, ROLE_CHANGE, WORKLOAD_ADJUSTMENT
    action_taken = Column(Text)
    assigned_to = Column(String(100)) # HR Name
    status = Column(String(20), default="Open") # Open, In-Progress, Closed
    
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)