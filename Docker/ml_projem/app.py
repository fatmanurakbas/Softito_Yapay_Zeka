from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import joblib


app = FastAPI()

model = joblib.load("churn_model.pkl")


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
    return {"message": "Churn Prediction API"}


@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([customer.dict()])

    prediction = model.predict(data)[0]

    return {
        "prediction": int(prediction)
    }