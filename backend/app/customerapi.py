from typing import Optional

from fastapi import FastAPI
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json

app = FastAPI()

@app.get("/")
def home():
    return {"hi":"world"}

@app.get("/cart")
def read_root():
    return {"Hello": "World"}

@app.get("/sneakers/{sneaker_name}")
def read_item(sneaker_name: str):
    sneaker = {"sneaker_name": sneaker_name}
    sneaker_json = json.dumps(sneaker)
    #sneaker_json = jsonable_encoder(sneaker_json)
    return JSONResponse(content=sneaker_json)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
