import typing
from fastapi import (
    APIRouter,
    Request,
    Depends,
    Response
)

from app.db.session import get_db
from app.db.crud import (
    get_user,
    get_users,
    get_user_by_email,
    create_user,
    edit_user,
    delete_user
)
from app.db.schemas import (
    User,
    UserCreate,
    UserUpdate,
    UserOut
)
from app.core.authentication import (
    get_current_active_superuser,
    get_current_active_user
)

user_router = APIRouter()

user_router.post("/users", )