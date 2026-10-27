from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, employees, prediction, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI(title="WorkForce AI Pro - HR Intelligence")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(employees.router, prefix="/api/employees", tags=["Employees"])
app.include_router(prediction.router, prefix="/api/predict", tags=["AI Prediction"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])

@app.get("/")
def home():
    return {"message": "WorkForce AI Pro API Running - Enterprise Level"}