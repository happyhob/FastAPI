from fastapi import FastAPI, status, Depends, HTTPException
import models
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import auth
from auth import get_current_user
'''sqlalchemy
sqlalchemy??
- python에서 데이터베이스와 객체 지향적으로 상호작용할 수 있도록 해주는 ORM 라이브러리
- SQL문을 직쩝 쓰지 않고 Python 클래스를 사용해서 데이터베이스를 다룰 수 있게 해준다

sqlalchemy.orm??
ORM은 Object <-> Relational (DB Table) 간의 매핑

Session??
데이터베이스와의 대화(트랜잭션)를 관리하는 객체
DB에 데이터를 읽고 쓰기 위한 작업의 단위!


'''

app = FastAPI()
app.include_router(auth.router) # auth.py에서 만든 라우터를 메인 애플리케이션에 틍록하는 작업

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]


#status_code=status.HTTP_200_OK : 경로에서 성공적으로 처리될 경우 반환되는 HTTP 상태코드(명시적으로 작성)
@app.get("/",status_code=status.HTTP_200_OK)
async def user(user:user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Fails')
    return {"User": user}