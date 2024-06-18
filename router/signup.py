# signup.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from save.db import SessionLocal, User, hash_password
from pydantic import BaseModel
from datetime import datetime
from save.db import pwd_context
import re

router = APIRouter()

class Signup(BaseModel):
    name: str
    email: str
    password: str
    passwordConfirm: str
    birthdate: datetime

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

@router.post("/signup")
async def signup(signup_info: Signup, db: Session = Depends(get_db)):
    try:
        if not validate_email(signup_info.email):
            raise HTTPException(status_code=400, detail="유효하지 않은 이메일 형식입니다.")
        if signup_info.password != signup_info.passwordConfirm:
            raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")

        hashed_password = hash_password(signup_info.password)

        new_user = User(name=signup_info.name, email=signup_info.email, password_hash=hashed_password,
                        birthdate=signup_info.birthdate)
        db.add(new_user)
        db.commit()

        return {"message": "회원가입이 완료되었습니다."}

    except HTTPException as e:
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"회원가입 중 오류 발생: {e}")
