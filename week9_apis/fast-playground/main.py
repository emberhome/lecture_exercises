from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': 'Hooray!!'}


@app.get('/welcome')
def welcome(fn,ln):
    return {'message':f'Welcome {fn} {ln}'}
