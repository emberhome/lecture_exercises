FROM python:3.12.8-bullseye

WORKDIR /app

RUN pip install uvicorn fastapi

COPY . .

CMD uvicorn fast_app.main:app --host 0.0.0.0 --port $PORT
