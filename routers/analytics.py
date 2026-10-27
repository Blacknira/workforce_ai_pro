from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models.employee import Employee
from app.models.attrition import AttritionPrediction
from app.models.activity_log import ActivityLog

router = APIRouter()

@router.get("/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    total = db.query(Employee).count()
    high_risk = db.query(AttritionPrediction).filter(AttritionPrediction.risk_level=="High").count()
    dept_data = db.query(Employee.department, func.count(Employee.id)).group_by(Employee.department).all()
    
    return {
        "total_employees": total,
        "high_risk_count": high_risk,
        "department_wise": [{"dept": d[0], "count": d[1]} for d in dept_data],
        "attrition_rate": round((high_risk/total*100) if total>0 else 0, 2)
    }