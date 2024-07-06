from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2

# URLPatternForPostgres = 'postgresql://username:password@ipAddress/hostname/databaseName'
SQLALCHEMY_DATABASE_URL = 'postgresql:postgress:admin@locahost/thriftShop'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# DB_NAME = "thriftShop"
# DB_USER = "postgres"
# DB_PASSWORD = "admin"
# DB_HOST = "localhost"
# DB_PORT = "5432"
#
# def get_db_connection():
#     try:
#         conn = psycopg2.connect(
#             dbname=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             host=DB_HOST,
#             port=DB_PORT
#         )
#         return conn
#     except psycopg2.Error as e:
#         raise RuntimeError(f"Error Connecting to database : {e}")
