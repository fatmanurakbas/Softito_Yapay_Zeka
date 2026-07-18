from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import requests

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    String
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

app = FastAPI(title="Gateway API")
templates = Jinja2Templates(directory="templates")
# ------------------------
# DATABASE
# ------------------------

DATABASE_URL = (
    "postgresql://postgres:postgres@postgres:5432/churndb"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    model_name = Column(String)

    prediction = Column(Integer)

    probability = Column(Float)


Base.metadata.create_all(bind=engine)

# ------------------------
# INPUT MODEL
# ------------------------


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

    return {
        "service": "gateway"
    }


@app.post("/predict")
def predict(customer: Customer):

    payload = customer.model_dump()

    logistic = requests.post(
        "http://logistic:8000/predict",
        json=payload
    ).json()

    rf = requests.post(
        "http://random_forest:8000/predict",
        json=payload
    ).json()

    xgb = requests.post(
        "http://xgboost:8000/predict",
        json=payload
    ).json()

    db = SessionLocal()

    for result in [logistic, rf, xgb]:

        row = Prediction(
            model_name=result["model"],
            prediction=result["prediction"],
            probability=result["probability"]
        )

        db.add(row)

    db.commit()

    db.close()

    return {
        "logistic": logistic,
        "random_forest": rf,
        "xgboost": xgb
    }