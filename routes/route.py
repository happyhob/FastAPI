from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
'''mongoDB가 자체적으로 만든 ID를 식별하는데 사용'''
from bson import ObjectId


router= APIRouter()

# GET Request Method
@router.get("/")
async def get_todos():
    '''MongoDB에서 컬렉션 이름만 전달하고 do find라고'''
    todos = list_serial(collection_name.find())
    return todos
