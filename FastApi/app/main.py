from typing import Union
from fastapi import FastAPI
from app.contacInfo import models as contactInfoModel
from app.contacInfo import contactInfo as contacInfoApi
from app.products import products as productsApi
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Replace with the URL of your Angular app
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

contactInfoModel.Base.metadata.create_all(bind=engine)

app.include_router(contacInfoApi.router)
app.include_router(productsApi.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


