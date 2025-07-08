from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'running': True}

@app.get("/sum_of_two")
def sum_of_two(a: int, b: int):
    return {'sum': a + b}
