from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import pandas as pd
from xgboost import XGBRegressor

# -----------------------------------
# APP
# -----------------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# DATA
# -----------------------------------
df = pd.read_csv("f1_features.csv")

features = [
    'grid_pos',
    'avg_last5',
    'team_strength',
    'driver_overtake_skill',
    'track_type_power',
    'track_type_street'
]

race_id = df['race'].max()

train_df = df[df['race'] < race_id]
test_df = df[df['race'] == race_id].copy()

# -----------------------------------
# MODEL
# -----------------------------------
model = XGBRegressor(n_estimators=150, learning_rate=0.08)
model.fit(train_df[features], train_df['finish_pos'])

# -----------------------------------
# ROUTES
# -----------------------------------
@app.get("/")
def home():
    return {"message": "F1 API running 🚀"}


@app.get("/predict")
def predict():
    temp = test_df.copy()

    temp['predicted_pos'] = model.predict(temp[features])
    temp = temp.sort_values(by='predicted_pos')
    temp['predicted_rank'] = range(1, len(temp)+1)

    return temp[['driver', 'predicted_rank', 'grid_pos']].to_dict(orient='records')


# -----------------------------------
# 🎮 SIMULATION MODELS
# -----------------------------------
class DriverInput(BaseModel):
    driver: str
    grid_pos: float

class SimulationInput(BaseModel):
    drivers: List[DriverInput]


@app.post("/simulate")
def simulate(data: SimulationInput):

    input_df = pd.DataFrame([d.dict() for d in data.drivers])

    merged = pd.merge(
        input_df,
        df,
        on="driver",
        how="left"
    )

    merged['predicted_pos'] = model.predict(merged[features])

    merged = merged.sort_values(by='predicted_pos')
    merged['predicted_rank'] = range(1, len(merged)+1)

    return merged[['driver', 'predicted_rank', 'grid_pos']].to_dict(orient='records')