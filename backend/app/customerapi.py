from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"hi":"world"}

@app.get("/cart")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
