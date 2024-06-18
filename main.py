# main.py

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from save.db import SessionLocal, engine
from router.signup import router as signup_router
from router.login import router as login_router
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(signup_router)
app.include_router(login_router)


@app.get("/")
async def welcome(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/home.do")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login.do")
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/new.do")
async def home(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
