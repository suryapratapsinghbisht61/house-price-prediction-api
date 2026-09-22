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
    Avebedrms:float= Field(gt=0, description="Average  bed rooms")
    AveOccup:float= Field(gt=0, description="Average  occupancy")
    Population:float= Field(gt=0, description="Average population ")
    Latitude:float= Field(ge=32, le=42, description="latitude")
    Longitude:float= Field(ge=-125, le=114, description="longitude")
    
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
        "features":features,
        "Features":"$39,000"
    }

#predict

@app.post("/predict")
def predict(house:HouseFefatures):
    try:
        input_datat=pd.DataFrame([{
            "MedInc":house.MedInc,
            "HouseAge":house.HouseAge,
            "AveRooms":house.AveRooms,
            "AveBedrms":house.Avebedrms,
            "Population":house.Population,
            "AveOccup":house.AveOccup,
            "Latitude":house.Latitude,
            "Longitude":house.Longitude,
            
        }])
        prediction=model.predict(input_datat)[0]
        price_usd=prediction*100000
        
        return{
            "predicted price":f"${price_usd:,.0f}",
            "predicted price short":f"${prediction:,.2f} hundred thousend ",
            "fidence range":f"${price_usd-39000:,.0f} to ${price_usd + 39000:,.0f}"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"prediction fail {str(e)}"
        )