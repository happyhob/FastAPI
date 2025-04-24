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

# POST Request Method
@router.post("/")
async def post_todo(todo:Todo):
    collection_name.insert_one(dict(todo))

# PUT Request Method
@router.put('/{id}')
async def put_todo(id: str, todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})

# Delete Request Method

@router.delete("/{id}")
async def delate_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})