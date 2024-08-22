from typing import Union
from fastapi import FastAPI, status, HTTPException
from app.contacInfo import models as contactInfoModel
from app.contacInfo import contactInfo as contacInfoApi
from app.products import products as productsApi
from app.users import users as usersApi
from app.users import auth as authApi
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
import uvicorn

app = FastAPI()

# app.include_router(authApi.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Replace with the URL of your Angular app
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

contactInfoModel.Base.metadata.create_all(bind=engine)

app.include_router(usersApi.router)
app.include_router(contacInfoApi.router)
app.include_router(productsApi.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)