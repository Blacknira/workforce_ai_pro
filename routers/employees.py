from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate

router = APIRouter()

@router.post("/")
def add_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    new_emp = Employee(**data.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.get("/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    return db.query(Employee).filter(Employee.id == emp_id).first()