from pydantic import BaseModel
from datetime import date
from fastapi import UploadFile, File

class BookBase(BaseModel):
    title: str = None
    author: str = None
    publish_date: date = None
    isbn: str = None
    price: float = None

class Book(BookBase):
    image_link: str
    id: int
    
    class Config:
        orm_mode = True

class BookCreate(BookBase):

    class Config:
        orm_mode = True

class BookUpdate(BookBase):

    class Config:
        orm_mode = True

class BookFilter(BaseModel):
    author: str = None
    publish_date: date = None

    class Config:
        orm_mode = True

class BookOut(BookBase):
    pass