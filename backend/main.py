from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# ✅ Enable CORS for local development (React app on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 👈 Only allow frontend on this origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your ML model
model = joblib.load("model.pkl")

# Define request schema
class LeadData(BaseModel):
    industry: str
    company_size: int
    region: str
    num_contacts: int
    engagement_score: int
    source: str

# Prediction endpoint
@app.post("/predict")
def predict(data: LeadData):
    # Convert input to DataFrame
    df = pd.DataFrame([data.dict()])

    # Dummy encoding for now (you can replace with actual preprocessing)
    df_encoded = pd.DataFrame({
        'industry': [1],  # Placeholder values
        'company_size': [data.company_size],
        'region': [2],
        'num_contacts': [data.num_contacts],
        'engagement_score': [data.engagement_score],
        'source': [3]
    })

    # Predict probability
    prob = model.predict_proba(df_encoded)[0][1]
    label = "Hot" if prob > 0.75 else "Warm" if prob > 0.4 else "Cold"

    return {"score": round(prob, 2), "label": label}
