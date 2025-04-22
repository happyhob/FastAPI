from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1, max_length=100)
    description: str = Field(min_length=1,max_length=100)
    rating: int = Field(gt=-1, lt=101) #0~100사이의 정수가 됨

BOOKS = []

@app.get("/")
def read_api1():
    return {'wellcome':'eric'}

@app.get("/{name}")
def read_api2(name:str):
    return {'wellcome':name}

@app.get("/book")
def read_api3():
    return BOOKS

@app.post("/")
def create_book(book:Book):
    BOOKS.append(book)
    print(BOOKS)
    return book


@app.put("/{book_id}")
def update_book(book_id:UUID, book: Book):
    counter = 0


    #BOOKS를 모두 반복하여 해당 UUID와 같은 값을 찾아서 입력받은 값으로 변환
    for x in BOOKS:
        counter+=1
        if x.id ==book.id:
            BOOKS[counter -1] = book
            return BOOKS[counter-1]
    #해당 uuid를 찾지 못할 때, 예외처리
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id}: Does not exist"
    )