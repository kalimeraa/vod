# Dockerfile
FROM python:3.9-slim

COPY requirements.txt /genre-service/requirements.txt

WORKDIR /genre-service

RUN pip install -r requirements.txt

COPY . /genre-service

ENTRYPOINT ["python"]

CMD ["app.py"]
