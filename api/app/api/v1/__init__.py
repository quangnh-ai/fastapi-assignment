from api.v1.users import user_router
from api.v1.auth import authentication_router
from api.v1.book import book_router

__all__ = [
    user_router,
    authentication_router,
    book_router
]