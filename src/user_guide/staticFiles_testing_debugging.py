from fastapi import FastAPI, HTTPException, status, Header
# from typing import H
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
# app = FastAPI(
#     title="ChimichangApp",
#     description=description,
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact=dict(
#         name="Deadpoolio the Amazing",
#         url="http://x-force.example.com/contact",
#         email="dp@x-force.example.com",
#     ),
#     license_info=dict(
#         name="Apache 2.0", url="https://www.apache.org/licenses/LICENSE-2.0.html"
#     ),
#     openapi_tags=tags_metadata,
#     openapi_url="/api/v1/openapi.json",
#     docs_url="/hello-world",
#     redoc_url=None,
# )
# app.mount("/static", StaticFiles(directory="static"), name="static")
fake_secret_token = "coneofsilence"
fake_db = dict(
    foo=dict(
        id = "foo", title="Foo", description="There goes my hero",

    ),
    bar = dict(
        id="bar", title="Bar", description="The bartenders"
    )
)

class Item(BaseModel):
    id: str
    title: str
    description: str | None = None



@app.get("/items/{item_id}",  response_model=Item)
async def read_main(item_id: str, x_token: str = Header(...)):
    if x_token != fake_secret_token: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid X-Token header")
    # item=fake_db.get(item_id)
    # if item is None
    if item_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item not found")
    return fake_db[item_id]


@app.post("/items/{item_id}", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists")
    
    fake_db[item.id] = item
    return item