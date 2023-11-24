from sqlalchemy import (
    Float, 
    Column,
    Integer, 
    String,
    Date
)
from db.models.base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String)
    publish_date = Column(Date)
    isbn = Column(String, unique=True, nullable=False)
    price = Column(Float)
    image_link = Column(String)