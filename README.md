California Housing Price Prediction API

A machine learning project that predicts California housing prices using the California Housing dataset and a Random Forest Regressor.

Project Overview

The model is trained using Scikit-learn and evaluated using MAE and R² score. After training, the model is saved with Joblib, so it can be loaded and used without retraining every time.

The trained model is then deployed through FastAPI, allowing clients or AI agents to send housing information through an API and receive a predicted house price.

Technologies Used

Python

Scikit-learn

Pandas

Joblib

FastAPI

Pydantic

Uvicorn

API Endpoints

GET / — API status

GET /helth — Model and API information

POST /predict — Predict house price from housing features

Project Structure
california-house-price-api/
├── train.py
├── main.py
├── house_model.joblib
├── house_features.joblib
├── requirements.txt
└── README.md

Run the Project

Install dependencies:

pip install -r requirements.txt


Start the API:

uvicorn main:app --reload


Then open /docs to test the API using FastAPI's interactive documentation.