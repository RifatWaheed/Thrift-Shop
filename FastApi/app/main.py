from typing import Union
from fastapi import FastAPI
from app.contacInfo import models as contactInfoModel
from app.contacInfo import contactInfo as contacInfoApi
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

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/contactInfo")
def contactInfo():
    return {"contactInfo Api"}
