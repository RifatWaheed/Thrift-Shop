from fastapi import FastAPI
from app.database import engine


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}