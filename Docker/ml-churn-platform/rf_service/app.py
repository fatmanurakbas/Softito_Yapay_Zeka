from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Random Forest Service")

model = joblib.load("random_forest.pkl")


class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {"service": "random_forest"}


@app.post("/predict")
def predict(customer: Customer):

    df = pd.DataFrame([customer.model_dump()])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "model": "random_forest",
        "prediction": int(prediction),
        "probability": float(probability)
    }