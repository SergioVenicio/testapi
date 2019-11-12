from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database


DATABASE_URL = 'postgresql://fastapi_user:fastapi@localhost:5432/fastapi'

engine = create_engine(
    DATABASE_URL,
)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()

