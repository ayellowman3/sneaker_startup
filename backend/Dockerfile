FROM python:3.8

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /backend/app /app

CMD [ "python", "/app/customerapi.py"]
