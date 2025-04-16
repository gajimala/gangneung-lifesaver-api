from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS 설정 (모든 도메인 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터 로드
with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

# 라우터 설정
@app.get("/lifesavers")
def read_lifesavers():
    return lifesavers
