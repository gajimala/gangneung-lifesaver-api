from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# 정적 파일 서빙 경로 등록
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# lifesavers.json 파일을 정확히 열어서 데이터 로드
DATA_FILE = os.path.join(os.path.dirname(__file__), "lifesavers.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/api")
def read_root():
    return {"message": "인명구조함 API 동작 중"}

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers

# HTML 파일 제공 (퍼블릭 폴더 내 파일)
@app.get("/lifesaver-map-naver")
def get_lifesaver_map():
    try:
        # public 폴더에 있는 lifsaver-map-naver.html 파일을 불러옵니다.
        with open("public/lifesaver-map-naver.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        return {"error": "HTML file not found"}
