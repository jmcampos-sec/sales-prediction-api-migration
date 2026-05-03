from fastapi import FastAPI
from app.models import SalesPrediction, PredictionResponse
import random

app = FastAPI(
    title="ABC Analytics - Sales Prediction API",
    description="API de predicción de ventas migrada a Azure",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "ABC Analytics API funcionando en Azure"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict_sales(data: SalesPrediction):
    prediction = round(data.base_sales * (1 + random.uniform(-0.1, 0.3)), 2)
    return PredictionResponse(
        product=data.product,
        predicted_sales=prediction,
        confidence=round(random.uniform(0.75, 0.95), 2)
    )