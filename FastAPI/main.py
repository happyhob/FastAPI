from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models

'''애플리케이션 _ CORS 정리
🔍 CORS란?
CORS (교차 출처 리소스 공유) 는 웹 브라우저에서 다른 출처(도메인, 포트, 프로토콜)의 자원에 접근할 수 있도록 허용하거나 차단하는 보안 정책입니다.

예를 들어:

프론트엔드: http://localhost:3000

백엔드 API (FastAPI): http://localhost:8000

이런 경우, 서로 출처(origin) 가 다르므로, 브라우저는 CORS 정책에 따라 기본적으로 요청을 차단합니다.
-------------------------------------------------------------------------------------------------

📌 왜 CORSMiddleware가 필요한가?
프론트엔드 (React, Vue 등)에서 FastAPI API 서버로 데이터를 요청할 때, 서로 다른 도메인일 가능성이 높습니다.

이를 해결하려면 FastAPI 서버가 "나는 이 출처에서 오는 요청을 허용해!" 라고 명시적으로 알려야 합니다.
그 역할을 CORSMiddleware가 해줍니다.


'''
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
)


class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    data:str

class TransactionModel(TransactionBase):
    id: int

    class Config:
        #orm_mode = True        # Pydantic 버전 V1
        from_attributes = True  # Pydantic 버전 V2

# 무조건 DB Session을 만들면 반납해야하기때문에!!!
def get_db():
    db =SessionLocal()

    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)


@app.post("/transactions/",response_model = TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_dependency):
    #Base의 모든 변수를 transaction 테이블로 매핑하여 sqlite 데이터베이스에 저장
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@app.get("/transactions", response_model = List[TransactionModel])
async def read_transactions(db: db_dependency, skip: int =0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions