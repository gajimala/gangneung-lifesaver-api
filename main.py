from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
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

# JSON 파일을 읽어서 데이터 로드
with open(DATA_FILE, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers  # JSON 데이터를 반환

# /lifesaver-map-naver 경로에서 HTML 파일 서빙
@app.get("/lifesaver-map-naver")
def get_lifesaver_map():
    with open("public/lifesaver-map-naver.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)  # HTML 파일을 반환
