from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import ENGINE
from model import ProductInfo, UserInfo
from sqlalchemy.orm import sessionmaker
session_factory = sessionmaker(bind=ENGINE)

app = FastAPI()

from pydantic import BaseModel

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------API------------
# 테이블에 있는 모든 사용자 정보 GET
@app.get("/product")
def read_users():
    with session_factory() as session:
        prod = session.query(ProductInfo).all()
        return prod

@app.get("/users/{user_id}")
def read_user(user_id: int):
    with session_factory() as session:
        user = session.query(UserInfo).\
            filter(UserInfo.userID == user_id).limit(1).all()
        return user

