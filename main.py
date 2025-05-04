import json
import os
import time
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 👉 정적 파일 서빙: /static 경로로 public 폴더 내용
app.mount("/static", StaticFiles(directory="public"), name="static")

# 👉 루트 접속 시 index.html 반환
@app.get("/")
def root():
    return FileResponse("public/index.html")

# 👉 구조 요청 파일 위치
REQUESTS_FILE = "/tmp/requests.json"

class HelpRequest(BaseModel):
    lat: float
    lon: float
    timestamp: float  # milliseconds

# 👉 구조요청 POST 처리
@app.post("/request-help")
def request_help(data: HelpRequest):
    try:
        print("📥 구조요청 수신됨:", data.dict())

        if not os.path.exists(REQUESTS_FILE):
            with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)

        with open(REQUESTS_FILE, "r", encoding="utf-8") as f:
            requests = json.load(f)

        now = time.time() * 1000
        # 최근 24시간 이내 요청만 유지
        recent = [r for r in requests if now - r.get("timestamp", 0) < 86400000]
        recent.append(data.dict())

        with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
            json.dump(recent, f, ensure_ascii=False, indent=2)

        return {"status": "ok", "count": len(recent)}

    except Exception as e:
        print("❌ 오류 발생:", e)
        return {"status": "error", "message": str(e)}

# 👉 구조요청 데이터 제공 (GET)
@app.get("/requests.json")
def serve_requests():
    return FileResponse(REQUESTS_FILE, media_type="application/json")

# 👉 lifesavers.json 제공
@app.get("/lifesavers")
def serve_lifesavers():
    try:
        with open("public/lifesavers.json", encoding="utf-8") as f:
            data = json.load(f)

        # Kakao와 Naver 모두 'lng' 필드 사용하게 통일
        for item in data:
            if "lon" in item:
                item["lng"] = item.pop("lon")

        return data

    except Exception as e:
        return {"status": "error", "message": str(e)}
