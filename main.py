from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json
import os

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

# lifesaver 데이터 로드 (전국 좌표만, 오류 로깅 포함)
json_path = os.path.join(os.path.dirname(__file__), "nationwide_lifesavers_coordinates_only.json")

try:
    with open(json_path, "r", encoding="utf-8") as f:
        lifesavers = json.load(f)
except Exception as e:
    print("🔥 JSON 로딩 실패:", e)
    lifesavers = []

@app.get("/api")
def read_root():
    return {"message": "전국 인명구조함 API (좌표만) 동작 중"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
