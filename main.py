from pydantic import BaseModel
import time

REQUESTS_FILE = "public/requests.json"

class HelpRequest(BaseModel):
    lat: float
    lon: float
    timestamp: float  # ms 단위

@app.post("/request-help")
def request_help(data: HelpRequest):
    try:
        # 파일이 없으면 생성
        if not os.path.exists(REQUESTS_FILE):
            with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)

        # 기존 요청 불러오기
        with open(REQUESTS_FILE, "r", encoding="utf-8") as f:
            requests = json.load(f)

        # 24시간 이내 데이터만 유지 (밀리초 기준)
        now = time.time() * 1000
        valid_requests = [r for r in requests if now - r["timestamp"] < 86400000]

        # 새 요청 추가
        valid_requests.append(data.dict())

        # 다시 저장
        with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
            json.dump(valid_requests, f, ensure_ascii=False, indent=2)

        return {"status": "ok", "count": len(valid_requests)}

    except Exception as e:
        return {"status": "error", "message": str(e)}
