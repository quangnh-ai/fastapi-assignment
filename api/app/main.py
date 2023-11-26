from fastapi import FastAPI, Depends
from starlette.requests import Request
import logging
from logging.handlers import TimedRotatingFileHandler

from core import config
from core.authentication import get_current_active_user
from api.v1 import (
    user_router, 
    authentication_router, 
    book_router,
    celery_router
)
from db.session import session_local

app = FastAPI(
    title=config.API_TITLE,
    openapi_url=config.API_OPENAPI_URL,
    docs_url=config.API_DOCS_URL,
    redoc_url=config.API_REDOC_URL
)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = TimedRotatingFileHandler('/logs/{}-{}-{}_{}h-00p-00.log'.format(
    config.u.year, config.u.month, config.u.day , config.u.hour), when="midnight", interval=1, encoding='utf8')
handler.suffix = "%Y-%m-%d"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = session_local()
    response = await call_next(request)
    request.state.db.close()
    return response

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
    celery_router,
    prefix="/api/v1/celery",
    tags=["V1 Celery"]
)

app.include_router(
    authentication_router, 
    prefix="/api", 
    tags=["auth"]
)