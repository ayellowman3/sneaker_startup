FROM python:3.8

WORKDIR /fastapi-app

COPY requirements.txt .
COPY app/sneakers/ sneakers/

RUN pip install -r requirements.txt

COPY ./app /app

CMD [ "python", "/app/client.py"]
