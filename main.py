from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
import os

app = FastAPI()

# JSON 데이터 로드
DATA_FILE = os.path.join(os.path.dirname(__file__), "nationwide_lifesavers_coordinates_only.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

# /lifesavers 경로 설정 (JSON 데이터 반환)
@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers

# /lifesaver-map-naver 경로에서 HTML 파일 제공
@app.get("/lifesaver-map-naver")
def get_lifesaver_map():
    with open("lifesaver-map-naver.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# / 경로 설정 (기본 홈 페이지 반환)
@app.head("/")
def head_root():
    return {"message": "홈페이지로 연결되었습니다!"}

