# Dockerfile
FROM python:3.9-slim

COPY requirements.txt /content-service/requirements.txt

WORKDIR /content-service

RUN pip install -r requirements.txt

COPY . /content-service

ENTRYPOINT ["python"]

CMD ["app.py"]
