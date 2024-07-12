import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.model import Base

load_dotenv()  # Load environment variables from .env

DATABASE_URL = os.getenv('DATABASE_URL')

# SQLite 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)

# 데이터베이스 세션 생성기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 데이터베이스 초기화 함수
def init_db():
    Base.metadata.create_all(bind=engine)
