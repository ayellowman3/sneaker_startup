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
    with open("cart.txt", "r+") as cart:
        return(cart.read())

@app.get("/cart")
def read_root():
    return {"Hello": "World"}

@app.get("/sneakers/{sneaker_id}")
def add_to_cart(sneaker_id: str):
    sneaker = {"sneaker_id": sneaker_id}
    with open("cart.txt", 'a') as cart:
        print(sneaker_id)
        cart.write(sneaker_id + '\n')

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
