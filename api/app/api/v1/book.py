import typing
from fastapi import (
    APIRouter,
    Depends,
    status
)

from db.session import get_db
from db.crud import (
    create_book,
    get_book_by_id,
    get_all_books,
    get_book_by_title,
    get_book_by_isbn,
    get_books_by_author,
    get_books_by_publish_date,
    update_book,
    delete_book
)
from db.schemas import (
    Book,
    BookCreate,
    BookUpdate
)
from core.authentication import (
    get_current_active_superuser,
    get_current_active_user
)

book_router = APIRouter()

@book_router.post(
    "/create",
    response_model=Book,
    name="Create book",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create(
    *,
    book: BookCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return create_book(db, book)

@book_router.get(
    "/get/id/{book_id}",
    response_model=Book,
    name="Get book by id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_book_info_by_id(
    *,
    book_id: int,
    db=Depends(get_db)
):
    return get_book_by_id(db, book_id)

@book_router.get(
    "/get/all",
    response_model=typing.List[Book],
    name="Get all books",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_books(
    db=Depends(get_db)
):
    return get_all_books(db)

@book_router.get(
    "/get/id/{book_id}",
    response_model=Book,
    name="Get book by id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_book_info_by_id(
    *,
    book_id: int,
    db=Depends(get_db)
):
    return get_book_by_id(db, book_id)

@book_router.get(
    "/get/title/{book_title}",
    response_model=Book,
    name="Get book by title",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_book_info_by_title(
    *,
    book_title: str,
    db=Depends(get_db)
):
    return get_book_by_title(db, book_title)

@book_router.get(
    "/get/isbn/{isbn}",
    response_model=Book,
    name="Get book by isbn",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_book_info_by_isbn(
    *,
    book_isbn: str,
    db=Depends(get_db)
):
    return get_book_by_isbn(db, book_isbn)

@book_router.get(
    "/get/author/{author}",
    response_model=typing.List[Book],
    name="Get books by author",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_book_info_by_author(
    *,
    author: str,
    db=Depends(get_db)
):
    return get_books_by_author(db, author)

@book_router.get(
    "/get/author/{publish_date}",
    response_model=typing.List[Book],
    name="Get book by publish date",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
def get_books_info_by_publish_date(
    *,
    publish_date: str,
    db=Depends(get_db)
):
    return get_books_by_publish_date(db, publish_date)

@book_router.put(
    "/update/{book_id}",
    response_model=Book,
    name="Update book",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update(
    *,
    book_id: str,
    book: BookUpdate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return update_book(db, book_id, book)