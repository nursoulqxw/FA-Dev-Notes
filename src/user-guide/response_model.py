from typing import Annotated, Any

from pydantic import BaseModel, EmailStr
from fastapi import FastAPI

app = FastAPI()

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user





#BaseUser has the base fields. Then UserIn inherits from BaseUser and adds the password field, so, it will include all the fields from both models.

#We annotate the function return type as BaseUser, but we are actually returning a UserIn instance.

#The editor, mypy, and other tools won't complain about this because, in typing terms, UserIn is a subclass of BaseUser, which means it's a valid type when what is expected is anything that is a BaseUser.


# class UserIn(BaseModel):
#     username: str
#     password: str 
#     email: EmailStr
#     full_name: str | None = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []


# Don't do this in production!
# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item

# @app.get("/items/", response_model=list[Item])
# async def read_item() -> Any:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]