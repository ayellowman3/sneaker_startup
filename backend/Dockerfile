FROM nginx:latest

WORKDIR /fastapi-app

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y
RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app /app

RUN touch cart.txt
RUN rm cart.txt
RUN touch cart.txt

RUN curl -s https://package.datadome.co/autoinstall_nginx_module.sh > \
    autoinstall_nginx_module.sh && bash autoinstall_nginx_module.sh

COPY nginx.conf .

EXPOSE 8000

CMD [ "python3", "/app/customerapi.py"]
