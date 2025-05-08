from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
'''
데이터 유효성 검사 및 직렬화/역직렬화를 위한 **기본 모델 클래스(BaseModel)**를 가져오는 코드

- 입력 데이터의 유효성 검사(validation)
- 타입 자동 변환
- 직렬화/역직렬화(JSON <-> Python 객체)
- 자동 완성/문서화 지원 (FastAPI 등에서 유용)

데이터베이스 연결, 인증, 공통 로직 등을 함수로 분리해서 필요한 곳에 자동으로 주입할 수 있게 도와줌
'''
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
FastAPI에서 사용하는 코드로, 
**의존성 주입(Dependency Injection)**을 통해 SQLAlchemy 세션을 뷰 함수에 자동으로 전달하려고 할 때 사용

    - Annotated
    :Python의 typing.Annotated는 타입에 추가 정보를 부여할 수 있도록 도와주는 기능입니다.

    - Session
    :SQLAlchemy의 Session 객체로, 데이터베이스와의 연결(트랜잭션)을 다루는 객체입니다.

    - Depends(get_db)
    :FastAPI의 Depends는 의존성을 선언합니다. get_db라는 함수를 실행해서 그 리턴값(Session)을 이 자리에 주입해 줍니다.

Annotated[...]
Python 3.9+ 또는 typing_extensions.Annotated에서 지원.

기본 타입(Session)에 추가적인 메타정보(Depends(get_db))를 덧붙이는 방식입니다.

FastAPI는 이 Annotated 타입을 인식해서 의존성 주입을 처리합니다.
'''
db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/posts", status_code = status.HTTP_201_CREATED)
async def create_post(post:PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()    


@app.post("/users/", status_code = status.HTTP_201_CREATED)
async def create_user(user:UserBase, db: db_dependency):
    '''
    db_user = models.User(**user.dict())
    => FastAPI와 SQLAlchemy를 함께 사용할 때 Pydantic 모델(user)을 SQLAlchemy 모델(User)로 변환
    
    Pydantic 모델(Python 객체) → SQLAlchemy 모델(DB 객체) 로 변환

    **user.dict()는 딕셔너리 값을 키워드 인자(unpacking) 로 넘겨주는 문법
    '''
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}", status_code = status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code =404 ,detail='User not found')
    return user