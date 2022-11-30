from fastapi import FastAPI
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

def rm(prod, user_id):
    if user_id == 0:
        del prod[0]
        del prod[0]
        del prod[0]
    elif user_id == 1:
        del prod[3]
        del prod[3]
        del prod[8]
    elif user_id == 2:
        del prod[5]
        del prod[6]
        del prod[6]
    else:
        del prod[6]
        del prod[8]
        del prod[8]
    return prod

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
            filter(UserInfo.userID == user_id).all()

        prod = session.query(ProductInfo.name, ProductInfo.img, ProductInfo.price).all()

        prod = rm(prod, user_id)

        user.append({"other":prod})
        return user