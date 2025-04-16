from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터 로드
with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

# /lifesavers 엔드포인트
@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
