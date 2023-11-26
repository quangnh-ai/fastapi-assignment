from api.v1.users import user_router
from api.v1.auth import authentication_router
from api.v1.books import book_router
from api.v1.celery import celery_router

__all__ = [
    user_router,
    authentication_router,
    book_router,
    celery_router
]