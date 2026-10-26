from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My FastAPI API is Live!"}


@app.get("/about")
def about():
    return {"message": "This is my first deployed API"}