from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str]=set()
    image: List[Image] | None = None #submodel, we use it as the type of an attribute

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item] # sub-sub model



@app.post("/index-weight/")
async def create_index_weight(weights: dict[int, float]):
    return weights




#---------------3----------
# @app.post("/images/multiple/")
# async def create_multiple_images(images = list[Image]): # u can also declare here
#     for image in images:
#         image.url
#     return image


#--------------2--------------
# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer


#-------------1----------
# @app.put("/item/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results