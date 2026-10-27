from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.employee import Employee
from app.models.attrition import AttritionPrediction
from app.models.activity_log import ActivityLog
from app.ml.predictor import predict_attrition

router = APIRouter()

@router.post("/predict/{employee_id}")
def predict_employee_attrition(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return {"error": "Employee not found"}

    # AI Model call
    result = predict_attrition(employee)

    # Save prediction
    new_prediction = AttritionPrediction(
        employee_id=employee_id,
        risk_score=result["risk_score"],
        risk_level=result["risk_level"],
        factors=result["factors"],
        confidence=result["confidence"]
    )
    db.add(new_prediction)
    
    # Add to Activity Log
    log = ActivityLog(
        employee_id=employee_id,
        activity_type="ATTRITION_PREDICTED",
        description=f"Risk Level: {result['risk_level']} - Score: {result['risk_score']}%"
    )
    db.add(log)
    
    db.commit()
    db.refresh(new_prediction)

    return {
        "employee_name": employee.name,
        "risk_score": new_prediction.risk_score,
        "risk_level": new_prediction.risk_level,
        "factors": new_prediction.factors,
        "prediction_id": new_prediction.id
    }