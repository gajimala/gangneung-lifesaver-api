
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import json

app = FastAPI()

# 정적 파일 서비스
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON 경로를 명확하게 고정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "gangneung_lifesavers.json")

try:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        lifesavers = json.load(f)
except Exception as e:
    print("🔥 JSON 파일 로딩 실패:", e)
    lifesavers = []

@app.get("/api")
def read_root():
    return {"message": "인명구조함 API 동작 중"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
