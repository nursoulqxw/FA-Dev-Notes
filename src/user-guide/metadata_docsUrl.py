from fastapi import FastAPI

description = """
ChimichangApp API helps you to do awesome things. 

## Items

You can **read items**.

## Users

you will be able to:

* **create users** (_not implemented_).
* **read users** (_not implemented_).

"""

tags_metadata = [
    dict(name='users', 
          description="operations with users. the **login** logic is also here."
    ),

    dict(name='items',
         description="Manage items. So _fancy_ they have their own docs",
         externalDocs=dict(
             description="Items external docs",
             url="https://www.jvp.design"
         )
    ),
]

app = FastAPI(
    title="Chimichang app",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact=dict(
        name="Deadpoolio the Amazing",
        url="http://x-force.example.com/contact",
        email="dp@x-force.example.com",
    ),
    license_info=dict(
        name="Apache 2.0", url="https://www.apache.org/licenses/LICENSE-2.0.html"
    ),
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    # docs_url="/hello-world",
    # redoc_url=None,

)

@app.get('/users', tags=['users'])
async def get_users():
    return [dict(name="Harry"), dict(name="Ron")]

@app.get("/items", tags=['items'])
async def read_items():
    return [dict(name = "wand"), dict(name="flying broom")]