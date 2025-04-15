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

# JSON 파일 불러오기
with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/")
def root():
    return {"message": "Gangneung Lifesaver API is running."}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
