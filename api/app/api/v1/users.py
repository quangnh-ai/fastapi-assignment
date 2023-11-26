import typing
from fastapi import (
    APIRouter,
    Depends,
    status
)

from db.session import get_db
from db.crud import (
    get_user_by_id,
    get_users,
    get_user_by_email,
    create_user,
    update_user,
    delete_user
)
from db.schemas import (
    User,
    UserCreate,
    UserUpdate
)
from core.authentication import (
    get_current_active_superuser,
    get_current_active_user
)

user_router = APIRouter()

@user_router.post(
    "/create",
    response_model=User,
    name="Create user",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create(
    *,
    user: UserCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return create_user(db, user)

@user_router.put(
    "/update/{user_id}",
    response_model=User,
    name="Update user",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update(
    *,
    user_id: int,
    user: UserUpdate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return update_user(db, user_id, user)

@user_router.delete(
    "/delete/{user_id}",
    response_model=User,
    name="Delete user",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete(
    *,
    user_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return delete_user(db, user_id)

@user_router.get(
    "/get",
    response_model=typing.List[User],
    name="Get multiple users",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_multiple_users(
    *,
    skip: int=0,
    limit: int=0,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return get_users(db, skip, limit)

@user_router.get(
    "/get/id/{user_id}",
    response_model=User,
    name="Get user by ID",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_user_info_by_id(
    *,
    user_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return get_user_by_id(db, user_id)

@user_router.get(
    "/get/email/{user_email}",
    response_model=User,
    name="Get user by email",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_user_info_by_email(
    *,
    user_email: str,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    return get_user_by_email(db, user_email)

@user_router.get(
    "/get/current",
    response_model=User,
    name="Get current user",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_current_user(
    *,
    current_user=Depends(get_current_active_user)
):
    return current_user
    