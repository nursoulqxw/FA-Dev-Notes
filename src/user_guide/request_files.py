from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_files(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}