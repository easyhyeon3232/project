#db.py
from sqlalchemy import create_engine, Integer, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from passlib.context import CryptContext

# MySQL 데이터베이스 연결 정보 설정
DB_USER = "root"
DB_PASSWORD = "1234"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "newuser"

# SQLAlchemy 연결 URL 생성
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

# SQLAlchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 비밀번호 해싱 관련 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 사용자 모델
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)



# 비밀번호 해싱 함수
def hash_password(password: str) -> str:
    return pwd_context.hash(password)
