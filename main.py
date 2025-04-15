from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json
import os
import uvicorn

app = FastAPI()

app.mount("/", StaticFiles(directory="public", html=True), name="public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
    lifesavers_data = json.load(f)

@app.get("/lifesavers")
def get_lifesavers():
    return [
        {
            **item,
            "latitude": item["lat"],
            "longitude": item["lon"]
        }
        for item in lifesavers_data
    ]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)