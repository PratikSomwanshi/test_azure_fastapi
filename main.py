from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}


@app.get("/test")
def test():
    return "This is just for testing" 
