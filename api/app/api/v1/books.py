import os
import typing
from fastapi import (
    APIRouter,
    Depends,
    status,
    UploadFile,
    HTTPException,
    File
)
from fastapi.responses import StreamingResponse

from db.session import get_db
from db.crud import (
    create_book,
    get_book_by_id,
    get_all_books,
    get_book_by_title,
    get_book_by_isbn,
    get_books_by_author,
    get_books_by_publish_date,
    get_books_by_publish_month,
    get_books_by_publish_year,
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
from core import config
from utils import time, storage

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
    book: BookCreate = Depends(),
    file: UploadFile = File(...),
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="This file type is not supported"
        )
    file_name = book.isbn + ".jpg"
    file_path = os.path.join(config.STORAGE_PATH, file_name)
    file_bytes = file.file.read()
    storage.upload_file_bytes(file_bytes, file_path)
    image_link = "http://{HOST_IP}:{HOST_PORT}/api/v1/books/show_image/?path={file_path}".format(
        HOST_IP=config.HOST_IP, 
        HOST_PORT=config.HOST_PORT,
        file_path=file_path
    )
    return create_book(db, book, image_link)

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
    "/get/isbn/{book_isbn}",
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
    "/get/publish_date/{year}/{month}/{date}",
    response_model=typing.List[Book],
    name="Get book by publish date",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
def get_books_info_by_publish_date(
    *,
    year: int,
    month: int,
    date: int,
    db=Depends(get_db)
):
    return get_books_by_publish_date(db, year, month, date)

@book_router.get(
    "/get/publish_month/{year}/{month}",
    response_model=typing.List[Book],
    name="Get book by publish month",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
def get_books_info_by_publish_month(
    *,
    year: int,
    month: int,
    db=Depends(get_db)
):
    return get_books_by_publish_month(db, year, month)

@book_router.get(
    "/get/publish_year/{year}",
    response_model=typing.List[Book],
    name="Get book by publish year",
    status_code=status.HTTP_200_OK
)
def get_books_info_by_public_year(
    *,
    year: int,
    db=Depends(get_db)
):
    return get_books_by_publish_year(db, year)

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
    book: BookUpdate = Depends(),
    file: UploadFile = File(None),
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    if file is not None:
        db_book = get_book_by_id(db, book_id)
        isbn = db_book.isbn
        os.remove(os.path.join(config.STORAGE_PATH, isbn + '.jpg'))
        file_bytes = file.file.read()
        storage.upload_file_bytes(
            file_bytes,
            os.path.join(config.STORAGE_PATH, isbn + '.jpg')
        )
    return update_book(db, book_id, book)

# test upload file
@book_router.post(
    "/test/upload_file",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def test_upload_file(
    *,
    image: UploadFile=File(...)
):
    if image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="This file type is not supported"
        )
    

    time_now_utc = time.now_utc()
    file_name = image.filename
    dir_path = config.STORAGE_PATH + time.str_yyyy_mm_dd(time_now_utc)
    storage.create_path(dir_path)
    file_path = dir_path + "/" + file_name
    file_bytes = image.file.read()
    storage.upload_file_bytes(file_bytes, file_path)

    return {
        "image_link": "http://{HOST_IP}:{HOST_PORT}/api/v1/books/show_image/?path={file_path}".format(
            HOST_IP=config.HOST_IP, 
            HOST_PORT=config.HOST_PORT,
            file_path=file_path
        )
    }

@book_router.get("/show_image/")
async def show_image(
    *,
    path: str
):

    def iterfile():
        with open(path.replace("\\", "/"), mode="rb") as file_like:  
            yield from file_like  
    try:
        return StreamingResponse(iterfile(), media_type="image/jpeg")
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found"
        )