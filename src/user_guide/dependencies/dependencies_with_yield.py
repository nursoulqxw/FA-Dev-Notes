from typing import Annotated
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}



def get_username():
    try:
        yield "Rick"
    finally:
        print("Cleanup up before response is sent")


@app.get("/users/me")
def get_user_me(username: Annotated[str, Depends(get_username, scope="function")]):
    return username



# class OwnerError(Exception):
#     pass

# class InternalError(Exception):
#     pass

# def get_username():
#     try:
#         yield "Rick"
#     except OwnerError as e:
#         raise HTTPException(status_code=400, detail=f"Owner error: {e}")

# def get_username1():
#     try:
#         yield "Rick"
#     except InternalError:
#         print("Oops, we didn't raise again, Britney 😱")

# @app.get("/items/{item_id}")
# def get_item(item_id: str, username: Annotated[str, Depends(get_username1)]):
#     if item_id == "portal-gun":
#         raise InternalError(
#             f"The portal gun is too dangerous to be owned by {username}"
#         )
#     if item_id != "plumbus":
#         raise HTTPException(
#             status_code=404, detail="Item not found, there's only a plumbus here"
#         )
#     raise item_id

# @app.get("/items/{item_id}")
# def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
#     if item_id not in data:
#         raise HTTPException(status_code=400, detail="not in the list")
#     item = data[item_id]
#     if item["owner"] != username:
#         raise OwnerError(username)
#     return item