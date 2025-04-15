from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.mount("/", StaticFiles(directory="public", html=True), name="public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers_data = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers_data
