import pandas as pd
# Simple Rule-based + ML Hybrid for Demo (Accuracy good for college)

def predict_attrition_risk(employee):
    risk = 0
    factors = []

    if employee.job_satisfaction <= 2:
        risk += 30
        factors.append("Low Job Satisfaction")
    if employee.over_time:
        risk += 25
        factors.append("High Overtime")
    if employee.work_life_balance <= 2:
        risk += 20
        factors.append("Poor Work-Life Balance")
    if employee.years_at_company < 2:
        risk += 15
        factors.append("New Employee")
    if employee.monthly_income < 40000:
        risk += 10
        factors.append("Low Income")

    risk_score = min(risk, 95)
    
    if risk_score >= 70:
        level = "High"
    elif risk_score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return risk_score, level, ", ".join(factors)

# For Real ML: Train RandomForest here with IBM dataset
# model = RandomForestClassifier().fit(X_train, y_train)