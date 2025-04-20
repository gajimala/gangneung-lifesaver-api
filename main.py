from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

app.mount("/", StaticFiles(directory="public", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

file_path = os.path.join(os.path.dirname(__file__), "gangneung_lifesavers.json")
with open(file_path, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/api")
def read_root():
    return {"message": "인명구조함 API 동작 중"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
