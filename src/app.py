from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from src.feature_engineering import FeatureEngineer

app = FastAPI(title="Dubai Smart Grid Energy Prediction API")

# Trained model load karna
model = joblib.load("models/energy_model.pkl")

class EnergyInput(BaseModel):
    timestamp: str  # Jaise "2024-06-15 14:00:00"

@app.get("/")
def home():
    return {"message": "Dubai Smart Grid MLOps API is running live!"}

@app.post("/predict")
def predict_energy(data: EnergyInput):
    # 1. Input timestamp ko dataframe me badalna
    df = pd.DataFrame({"timestamp": [data.timestamp]})
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)
    
    # 2. Wohi Feature Engineering chalana jo training ke waqt chali thi
    fe = FeatureEngineer(country="US", mode="predict")
    df_processed = fe.transform(df)
    
    # 3. Model se prediction karwana
    prediction = model.predict(df_processed)
    
    return {
        "timestamp": data.timestamp,
        "predicted_energy_load_mw": float(prediction[0])
    }
