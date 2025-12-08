from datetime import datetime

from typing import Annotated

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Pork"
    signup_ts:  datetime | None = None
    friends : list[int] = []


external_data = {
    'id': '123',
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)

# def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
#     return f"Hello {name}"

# print(say_hello("nur"))
