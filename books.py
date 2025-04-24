from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from uuid import UUID

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

'''실행될 때 database와 table이 아직 없다면 생성된다. '''
models.Base.metadata.create_all(bind=engine)    

'''
    db인스턴스 생성 SessionLocal 인스턴스를 생성한 다음 인스턴스를 닫는다
    db연결 프로세스는 일반적으로 싱글톤 유형의 프로토콜
'''
def get_db():
    try:
        db = SessionLocal()
        yield db    #yield : 값을 반환하고 상태 유지! return 과 비슷한 기능이지만 동작 방식이 다르다
    finally:
        db.close()


class Book(BaseModel):
    # id:UUID
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1, max_length=100)
    description: str = Field(min_length=1,max_length=100)
    rating: int = Field(gt=-1, lt=101) #0~100사이의 정수가 됨

BOOKS = []

@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Books).all()

@app.post("/")
def create_book(book:Book, db:Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book


@app.put("/{book_id}")
def update_book(book_id:int, book: Book, db: Session= Depends(get_db)):

    '''first()를 하는 건 id값이 유일하기 때문에 하나를 반환하면, 더이상 검색을 할필요가 없기 때문에'''
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    print(book_model)
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail =f"ID {book_id}: Does not exist"
        )
    
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book


@app.delete("/{book_id}")
def delete_book(book_id:int, db: Session = Depends(get_db)):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail =f"ID {book_id} : Does not exist"
        )    
    
    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()


@app.delete("/")
def reset_db(db: Session = Depends(get_db)):
    db.query(models.Books).delete()
    db.commit()
    return {"message": "All data deleted"}