from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # ✅ 추가!
import json

app = FastAPI()

# ✅ 정적 파일 라우팅 설정
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON 데이터 로드
with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

# 기본 라우트
@app.get("/api")
def read_root():
    return {"message": "인명구조함 API 동작 중"}

# 인명구조함 위치 반환
@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
