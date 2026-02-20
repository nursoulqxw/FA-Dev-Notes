import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()

class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        return response 
    


origins = ["http://localhost:8000", "http://localhost:5173"]

app.add_middleware(MyMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=origins)

@app.get("/blah")
async def blah():
    return {"hello": "world"}