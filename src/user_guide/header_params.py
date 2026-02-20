from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

# app.get("/items/")
# async def read_items(
#         strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
# ):
#     return {"strange_header": strange_header}

# app.get("/items/")
# async def get_items(user_agent: Annotated[str | None, Header()] = None):
#     return {"User-Agent": user_agent}



# Automatic conversion¶
# Header has a little extra functionality on top of what Path, Query and Cookie provide.

# Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-).

# But a variable like user-agent is invalid in Python.

# So, by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.

# Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case").

# So, you can use user_agent as you normally would in Python code, instead of needing to capitalize the first letters as User_Agent or something similar.
