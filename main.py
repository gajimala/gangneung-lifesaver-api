from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/")
def root():
    return {"message": "Gangneung Lifesaver API is running"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers