from fastapi import FastAPI
from app.database import engine
from app.ContactInfo import api as contactInfoApi
from app.ContactInfo import models as contactInfoModels


app = FastAPI()

app.include_router(contactInfoApi.router, prefix="/api", tags=["contactInfo"])

@app.get("/")
async def root():
    return {"message": "Hello, world!"}