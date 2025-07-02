from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load trained model
with open('../models/trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

class DeliveryRequest(BaseModel):
    delivery_distance_km: float
    num_items: int
    dispatch_delay_minutes: float
    order_hour: int
    order_dayofweek: int
    vehicle_type_Bike: int
    vehicle_type_Car: int
    traffic_level_Medium: int
    traffic_level_High: int

@app.post("/predict")
async def predict(request: DeliveryRequest):
    # Convert input to DataFrame
    input_data = pd.DataFrame([dict(request)])
    
    # Make prediction
    eta = model.predict(input_data)[0]
    
    return {"eta_minutes": round(eta, 1)}

@app.get("/")
async def health_check():
    return {"status": "active", "message": "Delivery ETA Prediction System"}