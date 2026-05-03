from pydantic import BaseModel

class SalesPrediction(BaseModel):
    product: str
    base_sales: float
    month: int

class PredictionResponse(BaseModel):
    product: str
    predicted_sales: float
    confidence: float