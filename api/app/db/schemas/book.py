from pydantic import BaseModel
from datetime import date

class BookBase(BaseModel):
    title: str = None
    author: str = None
    publish_date: date = None
    isbn: str = None
    price: float = None

class Book(BookBase):
    id: int
    
    class Config:
        orm_mode = True

class BookCreate(BookBase):

    class Config:
        orm_mode = True

class BookUpdate(BookBase):

    class Config:
        orm_mode = True

class BookOut(BookBase):
    pass