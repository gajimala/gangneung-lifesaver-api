from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

# lifesaver 데이터 로드
with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/api")
def read_root():
    return {"message": "인명구조함 API 동작 중"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers

@app.get("/nationwide")
def get_nationwide_lifesavers():
    with open("nationwide_lifesavers_cleaned.json", encoding="utf-8") as f:
        return json.load(f)
