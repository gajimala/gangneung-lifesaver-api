from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import json
import os

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
DATA_FILE = os.path.join(os.path.dirname(__file__), "nationwide_lifesavers_coordinates_only.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers

# HTML 파일 경로 확인 후 반환 (파일 경로 제대로 설정)
@app.get("/lifesaver-map-naver")
def get_lifesaver_map():
    # lifsaver-map-naver.html 파일이 현재 디렉토리(즉, main.py가 있는 곳)에 있어야 합니다.
    try:
        with open("lifesaver-map-naver.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        return {"error": "HTML file not found"}
