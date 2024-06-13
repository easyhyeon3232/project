from fastapi import APIRouter

from fastapi import Depends
# from db.session import get_db
from sqlalchemy.orm import Session

@app.get('/')
def read_root():
    return {"message": "회원가입되셨습니다!"}

@app.get('/about')
def read_about():
    return {"massage": "About Page"}