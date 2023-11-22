from pydantic import BaseModel
import typing

class UserBase(BaseModel):
    email: str = None
    first_name: str = None
    last_name: str = None
    is_active: bool = True
    is_superuser: bool = False

class UserOut(UserBase):
    pass

class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    password: typing.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True