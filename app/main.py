import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import logging

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Model path (Docker / Linux friendly)
# --------------------------------------------------
MODEL_PATH = Path("Models/Random_Forest.joblib")

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------
app = FastAPI(
    title="🍽️ Food Demand Prediction API",
    description="RandomForest modeli orqali buyurtmalar sonini (num_orders) bashorat qilish",
    version="1.0"
)

model = None

# --------------------------------------------------
# Load model on startup
# --------------------------------------------------
@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
        logger.info("Model muvaffaqiyatli yuklandi: %s", MODEL_PATH)
    except Exception as e:
        logger.error("Model yuklashda xatolik: %s", e)
        model = None

# --------------------------------------------------
# Input Schema (FEATURES)
# ❗ num_orders YO‘Q (TARGET)
# --------------------------------------------------
class FoodDemandInput(BaseModel):
    center_id: float
    checkout_price: float
    base_price: float
    emailer_for_promotion: float
    homepage_featured: float
    category: float
    cuisine: float
    price_diff: float
    price_diff_ratio: float
    price_diff_log: float
    checkout_price_log: float
    base_price_log: float
    num_orders_sqrt: float

# --------------------------------------------------
# Output Schema
# --------------------------------------------------
class FoodDemandPrediction(BaseModel):
    predicted_num_orders: float

# --------------------------------------------------
# Health endpoints
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "running",
        "model": "RandomForestRegressor",
        "task": "Food Demand Prediction"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------------------------------------
# Predict endpoint
# --------------------------------------------------
@app.post("/predict", response_model=FoodDemandPrediction)
def predict(data: FoodDemandInput):

    if model is None:
        raise HTTPException(status_code=500, detail="Model yuklanmagan")

    # Input -> DataFrame
    df = pd.DataFrame([data.model_dump()])

    try:
        prediction = model.predict(df)[0]
    except Exception as e:
        logger.error("Prediction xatoligi: %s", e)
        raise HTTPException(status_code=500, detail=str(e))

    logger.info("Predicted num_orders: %.2f", prediction)

    return FoodDemandPrediction(
        predicted_num_orders=round(float(prediction), 2)
    )
