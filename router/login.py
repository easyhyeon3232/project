from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from save.db import SessionLocal, User as UserModel, hash_password, pwd_context
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
import secrets
from router.signup import get_db

router = APIRouter()

# 세션 저장을 위한 딕셔너리 생성
sessions = {}

# 사용자 정보 모델
class User(BaseModel):
    email: str
    password_hash: str

# OAuth2 패스워드 베어러 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 비밀번호 해시 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 비밀번호 검증 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 이메일로 사용자 정보 가져오는 함수
def get_user(email: str, db: Session):
    return db.query(UserModel).filter(UserModel.email == email).first()

# 로그인 엔드포인트 (세션 기반)
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(SessionLocal)):
    try:
        user = db.query(UserModel).filter(UserModel.email == form_data.username).first()
        if not user or not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        # 세션 ID 생성
        session_id = secrets.token_hex(16)  # 랜덤한 세션 ID 생성
        sessions[session_id] = user.email    # 세션 ID와 사용자 이메일 매핑

        # 클라이언트에 세션 ID를 쿠키로 전달
        response = {"message": "Logged in successfully"}
        response.set_cookie(key="session_id", value=session_id, httponly=True, samesite="strict")

        return response

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"로그인 중 오류 발생: {str(e)}")

