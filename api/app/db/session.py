from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(
    autocommit=False, 
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db 
    finally:
        db.close()