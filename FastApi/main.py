from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.ProductModel import Product
import psycopg2

app = FastAPI()

origins = [
    "http://localhost:4200",  # URL of your Angular application
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/contactInfo")
async def getContactInfo():
    return {"message": "rifatwaheed@gmail.com"}


@app.post("/createProduct")
async def createProduct(product: Product):
    return product
