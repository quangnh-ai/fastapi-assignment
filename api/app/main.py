from fastapi import FastAPI, Depends
from starlette.requests import Request

from core import config
from core.authentication import get_current_active_user
from api.v1 import user_router, authentication_router, book_router

app = FastAPI(
    title=config.API_TITLE,
    openapi_url=config.API_OPENAPI_URL,
    docs_url=config.API_DOCS_URL,
    redoc_url=config.API_REDOC_URL
)


app.include_router(
    user_router,
    prefix="/api/v1/users",
    tags=["V1 Users"],
    dependencies=[Depends(get_current_active_user)],
)

app.include_router(
    book_router,
    prefix="/api/v1/books",
    tags=["V1 Books"]
)

app.include_router(
    authentication_router, 
    prefix="/api", 
    tags=["auth"]
)