from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 NEW
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# 👇 Enable CORS (Allows frontend at different origin to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://localhost:3000"] later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")

class LeadData(BaseModel):
    industry: str
    company_size: int
    region: str
    num_contacts: int
    engagement_score: int
    source: str

@app.post("/predict")
def predict(data: LeadData):
    df = pd.DataFrame([data.dict()])
    
    # Dummy encoding for now
    df_encoded = pd.DataFrame({
        'industry': [1],
        'company_size': [data.company_size],
        'region': [2],
        'num_contacts': [data.num_contacts],
        'engagement_score': [data.engagement_score],
        'source': [3]
    })
    
    prob = model.predict_proba(df_encoded)[0][1]
    label = "Hot" if prob > 0.75 else "Warm" if prob > 0.4 else "Cold"

    return {"score": round(prob, 2), "label": label}
