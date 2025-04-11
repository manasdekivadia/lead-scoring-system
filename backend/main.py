from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Enable CORS (update this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Request schema
class LeadData(BaseModel):
    industry: str
    company_size: int
    region: str
    num_contacts: int
    engagement_score: int
    source: str

# Prediction route
@app.post("/predict")
def predict(data: LeadData):
    df_encoded = pd.DataFrame({
        'industry': [1],  # Placeholder
        'company_size': [data.company_size],
        'region': [2],    # Placeholder
        'num_contacts': [data.num_contacts],
        'engagement_score': [data.engagement_score],
        'source': [3]     # Placeholder
    })

    prob = model.predict_proba(df_encoded)[0][1]
    label = "Hot" if prob > 0.75 else "Warm" if prob > 0.4 else "Cold"

    return {"score": round(prob, 2), "label": label}

# Optional local run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
