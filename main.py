from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json
import math

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 서빙
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# 전체 lifesavers 반환
@app.get("/lifesavers")
def get_lifesavers():
    with open("public/gangneung_lifesavers.json", encoding="utf-8") as f:
        data = json.load(f)
    return data

# 거리 계산 함수 (Haversine)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# 위치 기반 lifesaver 필터 API
@app.get("/lifesavers/nearby")
def get_nearby_lifesavers(lat: float = Query(...), lon: float = Query(...), radius: float = Query(5)):
    with open("public/gangneung_lifesavers.json", encoding="utf-8") as f:
        data = json.load(f)
    nearby = []
    for item in data:
        if "lat" in item and "lng" in item:
            dist = haversine(lat, lon, item["lat"], item["lng"])
            if dist <= radius:
                nearby.append(item)
    return nearby
