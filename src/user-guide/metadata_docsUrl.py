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

app = FastAPI(
    title="Chimichang app",
    description=description,
    version="0.0.1"
)