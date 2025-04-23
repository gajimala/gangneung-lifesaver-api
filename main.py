from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
import os

app = FastAPI()

# JSON 데이터 로드
DATA_FILE = os.path.join(os.path.dirname(__file__), "nationwide_lifesavers_coordinates_only.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    lifesavers = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return lifesavers

# HTML 파일 서빙 (StaticFiles 제거하고 직접 응답)
@app.get("/lifesaver-map-naver")
def get_lifesaver_map():
    with open("lifesaver-map-naver.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

