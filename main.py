from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 서비스 시엔 필요한 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers_data = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers_data
