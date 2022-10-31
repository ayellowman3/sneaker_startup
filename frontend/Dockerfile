FROM python:3.8

WORKDIR /fastapi-app

COPY requirements.txt .
COPY sneakers/ sneakers/

RUN pip install -r requirements.txt

COPY /frontend/app /app

CMD [ "python", "/app/client.py"]
