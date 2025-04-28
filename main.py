'''1. FastAPI 웹 프레임워크 사용용
- HTTPException : 요청 처리 중 오류가 발생했을 때 사용
- Depends : 의존성 주입을 사용할 때 사용(예: DB연결을 요청 처리 시 자동으로 주입)
'''
from fastapi import FastAPI, HTTPException, Depends
'''2. 데이터 모델 정의 (pydantic 사용)
    - BaseModel : pydantic의 기능으로 ,데이터 유효성 검사와 직렬화를 쉽게 해준다

'''
from pydantic import BaseModel

from typing import List, Annotated

'''3. SQLAlchemy 모델과 DB 연결
    - models: 정의된 DB 테이블을 표현한 PYTHON 파일
    - database : 데이터베이스 세션(SessionLocal)과 데이터베이스 엔진(engine)의 정의된 파일.
    - Session: SQLAlchemy ORM에서 데이터베이스와 통신할 때 사용하는 객체
'''
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    choice_text:str
    is_correct:bool


class QuestionBase(BaseModel):
    question_text:str
    choices:List[ChoiceBase]



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/questions/")
async def create_questions(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text = question.question_text)
