from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from save.db import SessionLocal, User as UserModel, hash_password, pwd_context
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt
from router.signup import get_db

router = APIRouter()

# JWT 설정
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 사용자 정보 모델
class User(BaseModel):
    email: str
    password_hash: str

# OAuth2 패스워드 베어러 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 비밀번호 해시 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 토큰을 생성하는 함수
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 비밀번호 검증 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 이메일로 사용자 정보 가져오는 함수
def get_user(email: str, db: Session):
    return db.query(UserModel).filter(UserModel.email == email).first()

# 로그인 엔드포인트
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = get_user(form_data.username, db)
        if not user:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        if not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        access_token = create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"로그인 중 오류 발생: {str(e)}")

