import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON 파일 절대경로로 안전하게 읽기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "gangneung_lifesavers.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
