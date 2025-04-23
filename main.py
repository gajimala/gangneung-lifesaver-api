from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

# 정적 파일 서빙 경로 등록
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# JSON 데이터 로드
DATA_FILE = os.path.join(os.path.dirname(__file__), "nationwide_lifesavers_coordinates_only.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers

@app.get("/lifesaver-map-naver")
def get_lifesaver_map():
    # Render에서 정적 파일 서빙이므로 static 폴더에 파일이 있어야 합니다.
    with open("static/lifesaver-map-naver.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
