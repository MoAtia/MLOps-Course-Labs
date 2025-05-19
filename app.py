from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import logging
from typing import Literal

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize FastAPI app
app = FastAPI()

# Define categorical and numerical columns
cat_cols = ["Geography", "Gender"]
num_cols = [
    "CreditScore", "Age", "Tenure", "Balance",
    "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary"
]

# Expected order of features
all_features = num_cols + cat_cols

# Load model and transformer
try:
    with open("models/model_production_mlops.pkl", "rb") as f:
        model = joblib.load(f)
    logging.info("Model loaded successfully.")

    with open("models/col_transf.pkl", "rb") as f:
        transformer = joblib.load(f)
    logging.info("Transformer loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model or transformer: {e}")
    raise

# Input schema
class CustomerData(BaseModel):
    CreditScore: float
    Age: float
    Tenure: float
    Balance: float
    NumOfProducts: int
    HasCrCard: Literal[0, 1]
    IsActiveMember: Literal[0, 1]
    EstimatedSalary: float
    Geography: str
    Gender: str

# Endpoints
@app.get("/")
def home():
    logging.info("Home endpoint accessed.")
    return {"message": "Welcome to the Churn Prediction API!"}

@app.get("/health")
def health():
    logging.info("Health check accessed.")
    return {"status": "ok"}



@app.post("/predict")
def predict(data: CustomerData):
    logging.info(f"Received data for prediction: {data.dict()}")

    try:
        # Create input in correct order
        input_data = [[getattr(data, col) for col in all_features]]
        logging.info(f"Ordered input data: {input_data}")
        input_data = pd.DataFrame(input_data, columns=all_features)
        # Transform input
        transformed = transformer.transform(input_data)
        logging.info("Data transformed successfully.")

        # Predict
        prediction = model.predict(transformed)
        prob = model.predict_proba(transformed)[0][1]
        logging.info(f"Prediction: {prediction[0]}, Probability: {prob}")

        return {
            "churn_prediction": int(prediction[0]),
            "churn_probability": round(prob, 4)
        }

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed.")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Change 8001 to your desired port

