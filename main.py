import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")

@app.get("/.well-known/assetlinks.json", response_class=FileResponse)
async def get_assetlinks():
    return FileResponse("path/to/assetlinks.json")
  
@app.get("/book")
async def get_book():
    return "details"
