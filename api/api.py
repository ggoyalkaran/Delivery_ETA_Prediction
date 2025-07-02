import requests

payload = {
    "delivery_distance_km": 4.2,
    "num_items": 3,
    "dispatch_delay_minutes": 12,
    "order_hour": 14,
    "order_dayofweek": 2,
    "vehicle_type_Bike": 1,
    "vehicle_type_Car": 0,
    "traffic_level_Medium": 1,
    "traffic_level_High": 0
}

response = requests.post("https://your-api-url/predict", json=payload)
print(response.json())  # {"eta_minutes": 28.5}