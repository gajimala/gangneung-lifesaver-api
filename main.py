import json
import os
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

REQUESTS_FILE = "public/requests.json"

class HelpRequest(BaseModel):
    lat: float
    lon: float
    timestamp: float  # 밀리초 기준 (Date.now()와 호환)

@app.post("/request-help")
def request_help(data: HelpRequest):
    try:
        # 요청 파일 없으면 생성
        if not os.path.exists(REQUESTS_FILE):
            with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)

        # 기존 요청 불러오기
        with open(REQUESTS_FILE, "r", encoding="utf-8") as f:
            requests = json.load(f)

        # 24시간 이내 요청만 유지
        now = time.time() * 1000  # 현재 시각 (밀리초)
        recent_requests = [
            r for r in requests if now - r.get("timestamp", 0) < 86400000
        ]

        # 새 요청 추가
        recent_requests.append(data.dict())

        # 파일 저장
        with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
            json.dump(recent_requests, f, ensure_ascii=False, indent=2)

        return {"status": "ok", "count": len(recent_requests)}

    except Exception as e:
        return {"status": "error", "message": str(e)}
