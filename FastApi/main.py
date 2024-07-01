from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

DB_NAME = "thriftShop"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "53"
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn
@app.get("/contactInfo")
async def getContactInfo():
    return {"message": "rifatwaheed@gmail.com"}
