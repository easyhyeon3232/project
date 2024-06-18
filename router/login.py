from fastapi import APIRouter, Depends, HTTPException, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from save.db import SessionLocal, User as UserModel, hash_password, pwd_context
from passlib.context import CryptContext
from pydantic import BaseModel

from datetime import datetime, timedelta
import jwt

router = APIRouter()

# 비밀번호 해시 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 데이터베이스 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 사용자 정보 모델
class User(BaseModel):
    email: str
    password_hash: str

# 비밀번호 검증 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 이메일로 사용자 정보 가져오는 함수
def get_user(email: str, db: Session):
    return db.query(UserModel).filter(UserModel.email == email).first()

# JWT 설정
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 토큰을 생성하는 함수
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 로그인 처리
@router.post("/login")
def login(request: Request, form_data: User, db: Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.email == form_data.email).first()
        if not user or not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        # 인증이 성공하면 JWT 토큰을 생성하여 클라이언트에게 반환
        access_token = create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"로그인 중 오류 발생: {str(e)}")