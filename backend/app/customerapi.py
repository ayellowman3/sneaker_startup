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
def return_cart():
    data = []
    with open("cart.txt", "r+") as cart:
        sneaker_ids = cart.readlines()
        for id in sneaker_ids:
            data.append(id[:-1])
    return json.dumps({'ids':data})

@app.get("/history")
def return_history():
    data = []
    with open("history.txt", "r+") as cart:
        sneaker_ids = cart.readlines()
        for id in sneaker_ids:
            data.append(id[:-1])
    return json.dumps({'ids':data})

@app.get("/sneakers/{sneaker_id}")
def add_to_cart(sneaker_id: str):
    print(datadome_validation())
    if datadome_validation():

        sneaker = {"sneaker_id": sneaker_id}
        with open("cart.txt", 'a') as cart:
            print(sneaker_id)
            cart.writelines(f'{sneaker_id}\n')

@app.post("/checkout")
def checkout():
    print(datadome_validation())
    if datadome_validation():
        data = []
        with open("cart.txt", "r+") as cart:
            sneaker_ids = cart.readlines()
            for id in sneaker_ids:
                data.append(id[:-1])

        with open("history.txt", 'a') as history:
            for sneaker_id in data:
                history.writelines(f'{sneaker_id}\n')

        open('cart.txt', 'w').close()


def datadome_validation():
    import requests

    url = "https://api.datadome.co/validate-request/"

    payload = "RequestModuleName=my_connector&ModuleVersion=1.0&ServerName=server12.domain.com&APIConnectionState=new&IP=62.35.12.13&Port=60200&TimeRequest=1494584456492817&Protocol=HTTP&Method=GET&ServerHostname=sub.domain.com&Request=%2Ffolder%2Ffile.php%3Fparam%3Dvalue&HeadersList=Host%2CConnection%2CPragma%2CCookie%2CCache-Control%2CUser-Agent&Host=sub.domain.com&UserAgent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F58.0.3029.96%20Safari%2F537.36&Referer=http%3A%2F%2Fsub.domain.com%2Fhome.php&Accept=text%2Fhtml%2Capplication%2Fxhtml%2Bxml%2Capplication%2Fxml%3Bq%3D0.9%2Cimage%2Fwebp%2C%2A%2F%2A%3Bq%3D0.8&AcceptEncoding=gzip%2C%20deflate%2C%20sdch&AcceptLanguage=fr-FR%2Cfr%3Bq%3D0.8%2Cen-US%3Bq%3D0.6%2Cen%3Bq%3D0.4&XForwardedForIP=62.35.64.32%2C32.36.35.24&Connection=keep-alive&Pragma=no-cache&Key=xCCFYH0QjAIXXnv&AcceptCharset=string&Origin=string&X-Requested-With=string&CacheControl=string&CookiesLen=0&AuthorizationLen=0&PostParamLen=0&ClientID=string&ContentType=string&From=string&X-Real-IP=string&Via=string&TrueClientIP=string"
    headers = {
        "ContentType": "application/x-www-form-urlencoded",
        "User-Agent": "ReadMe-API-Explorer",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        return True
    return False

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
