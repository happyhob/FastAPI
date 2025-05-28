from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

'''APIRouter???????
- APIRouter()는 FastAPI에서 라우터(경로)를 분리/관리할 수 있게 해주는 객체

- prefix='/auth': 이 라우터에 등록된 모든 경로 앞에 **/auth**가 자동으로 붙는다.

    예: @router.post("/login")이면 실제 경로는 **/auth/login**이 됩니다.    

- tags=['auth']: 이건 Swagger 문서에서 카테고리 이름으로 사용됩니다.

    ✔️ 목적: 인증 관련 API들을 별도의 라우터 파일로 분리해 유지 보수를 쉽게 하려는 것
'''


SECRET_KEY = '1321KDFA#kj!@sadzx1952@dv3#advSADf#!Wvdd1@#'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')   

'''비민번호 해싱 도구

# 비밀번호 해싱
hashed_password = bcrypt_context.hash("plain_password")

# 비밀번호 검증
is_valid = bcrypt_context.verify("plain_password", hashed_password)
'''

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/token')    
''' 토큰 기반 인증
OAuth2 방식의 토큰 인증을 구현할 떄 사용하는 의존성 설정 객체

🔍 상세 설명:
    - OAuth2PasswordBearer는 FastAPI가 제공하는 인증 방식 중 하나로,
        - 로그인 후 받은 토큰을 헤더에 넣어야만 접근이 가능한 보호된 라우터를 만들 때 사용합니다.

    - tokenUrl='/auth/token'는 토큰을 발급받기 위한 엔드포인트 URL을 의미합니다.
        - 예: 클라이언트는 /auth/token에 사용자명/비번을 POST해서 토큰을 받고,
        - 이후 요청 시 Authorization: Bearer <token> 형태로 헤더를 보냅니다.

from fastapi import Depends

# 보호된 엔드포인트 예시
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_bearer)):
    return {"token": token}


'''
# 토큰은 곧 생성할 api앤드포인트가 될 것이기 떄문에 off토큰이다
class CreateUserRequest(BaseModel):
    username:str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", status_code=status.HTTP_201_CREATED)
# db_dependency  : 의존성 주읩으로 SQLALchemy의 Session 객체를 받아온다.
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        username= create_user_request.username,
        hashed_password = bcrypt_context.hash(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()

'''create_user 함수의 내용 설명
create_user_model = Users(
    username= create_user_request.username,
    hashed_password = bcrypt_context.hash(create_user_request.password)
)

✅ 의미:
    - Users는 SQLAlchemy ORM 모델로, 사용자 테이블을 나타냄냄

    - 사용자가 보낸 평문 비밀번호(create_user_request.password)를 bcrypt_context.hash(...)를 사용해 해싱하고, 사용자명과 함께 새로운 Users 객체를 생성

    - bcrypt_context는 passlib으로 만든 비밀번호 해싱 도구입니다.

🔚 정리 요약

    이 함수는 클라이언트가 사용자 생성 요청을 보내면:

        1. 요청 JSON 데이터를 받음

        2. 비밀번호를 안전하게 해싱함

        3. SQLAlchemy 모델로 사용자 객체 생성

        4. DB에 저장하여 새로운 사용자를 생성함
'''


@router.post("/token", response_model = Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db:db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail = 'Could not validate user.')
    token = create_access_token(user.username, user.id, timedelta(minutes=20))  #imedelta(minutes=20): 20분 동안 토큰이 유지 된다. 이후에는 재로그인 해야함

    return {'access_token':token, 'token_type':'bearer'}


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()

    if not user:
        return False    
    if not bcrypt_context.verify(password, user.hashed_password):   # verify: 이자식이 하는 일은 비밀번호가 일치하는지 확인하는 것
        return False
    return user

#서버 - 클라이언트 ACCESS 토큰 생성
def create_access_token(username:str, user_id: int, expires_delta: timedelta):
    encode = {'sub':username, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta        #현재 시간과  + 20분의 시가을 더함
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail = 'Could not validate user.')
        return {'username':username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')