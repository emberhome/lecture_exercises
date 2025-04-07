from sqlalchemy import create_engine, text
from fastapi import FastAPI
import os

app = FastAPI()

SQLALCHEMY_DATABASE_URL = os.environ.get("DB_URL")

@app.get("/")
def read_root():
    engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

    # Use connection to execute the query
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"DB": str(result.fetchone())}
