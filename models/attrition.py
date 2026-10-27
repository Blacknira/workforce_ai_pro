from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class AttritionPrediction(Base):
    __tablename__ = "attrition_predictions"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    
    risk_score = Column(Float, nullable=False) # 0-100
    risk_level = Column(String(20), index=True) # Low, Medium, High, Critical
    
    # AI Explainability
    factors = Column(Text) # "Low Satisfaction, Overtime"
    confidence = Column(Float, default=0.85)
    
    # Workflow Status
    is_alert_sent = Column(Integer, default=0) # 0/1
    intervention_status = Column(String(20), default="Pending") # Pending, In-Progress, Resolved
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship (optional)
    # employee = relationship("Employee")