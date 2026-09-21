from fastapi import FastAPI , HTTPException
import pandas as pd 
import joblib
from pydantic import BaseModel , Field

app=FastAPI()

model=joblib.load("house/house_model.joblib")
features=joblib.load("house/house_features.joblib")

#input schema 
class HouseFefatures(BaseModel):
    MedInc:float = Field(gt=0, description="MediaN Incom of Neigbourhood")
    HouseAge:float= Field(gt=0, description="Average age fo house")
    AveRooms:float= Field(gt=0, description="Average  rooms")
    AveDedrms:float= Field(gt=0, description="Average  bed rooms")
    AveOccup:float= Field(gt=0, description="Average  occupancy")
    Population:float= Field(gt=0, description="Average population ")
    Latitude:float= Field(ge=32, le=42, description="latitude")
    Longitude:float= Field(ge=125, le=114, description="longitude")
    
@app.get("/")
def home():
    return{"message":"calefornial house predection api",
           "status":"active",
           "endpoint":"send POST request to /predict"
           }
    
@app.get("/helth")
def helth():
    return{
        "status":"running",
        "model":"RandomForestRegressor",
        "Features":"$39,000"
    }
    
