import typing

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db import models, schemas

def get_book_by_id(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return book

def get_book_by_title(db: Session, title: str):
    book = db.query(models.Book).filter(models.Book.title == title).first()
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return book

def get_books_by_publish_date(db: Session, publish_date: str):
    return db.query(models.Book).filter(models.Book.publish_date == publish_date).all()

def get_books_by_author(db: Session, author: str):
    return db.query(models.Book).filter(models.Book.author == author).all()

def get_book_by_isbn(db: Session, isbn: str):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return book

def get_all_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    if db.query(models.Book).filter(models.Book.title == book.title).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book's title is duplicated"
        )
    if db.query(models.Book).filter(models.Book.isbn == book.isbn).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="ISBN is duplicated"
        )
    db_book = models.Book(
        title=book.title,
        author=book.author,
        publish_date=book.publish_date,
        isbn=book.isbn,
        price=book.price
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    db.delete(book)
    db.commit()
    return book




