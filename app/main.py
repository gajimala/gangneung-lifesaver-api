from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

with open("gangneung_lifesavers.json", "r", encoding="utf-8-sig") as f:
    lifesavers = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Lifesaver API is running!"}

@app.get("/lifesavers")
def get_lifesavers():
    return JSONResponse(content=lifesavers)

app.mount("/public", StaticFiles(directory="public"), name="public")
