
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON 데이터 로드
with open("gangneung_lifesavers.json", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/")
def root():
    return {"message": "Hello, this is the lifesaver API!"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers
