# FastAPI와 상태 코드를 불러옵니다.
from fastapi import FastAPI, status
# Pydantic의 BaseModel과 필드 검증 데코레이터를 불러옵니다.
from pydantic import BaseModel, field_validator
# 선택적 타입 지정에 필요한 Optional 불러오기
from typing import Optional

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 아이템 데이터를 위한 Pydantic 모델 정의
class Item(BaseModel):
    name: str 
    description: Optional[str] = None  # 선택적 문자열 필드, 기본값은 None
    price: int 

    # 스웨거 UI에서 보여줄 예제 데이터 정의
    class Config:
        json_schema_extra = {
            'examples': [
                {
                    'name': 'Learn Pydantic v2',
                    'description': 'Watch codingwithroby tutorials',
                    'price': 1
                }
            ]
        }

    # 가격은 반드시 양수여야 함을 검증하는 메서드
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('The price must be positive')  # 0 이하일 경우 예외 발생
        return value  # 유효한 값이면 그대로 반환

# POST 요청으로 /items/ 경로에 아이템을 생성하는 엔드포인트
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    item_dict = item.model_dump()  # Pydantic 모델을 딕셔너리로 변환
    return {"item": item_dict}  # 생성된 아이템 데이터를 JSON으로 반환


'''
✅ @classmethod란?
@classmethod는 클래스 메서드를 정의할 때 사용하는 데코레이터입니다.
이 메서드는 클래스 자체(cls) 를 첫 번째 인자로 받아, 인스턴스가 아닌 클래스 수준에서 작동합니다.

🔁 일반 메서드 vs 클래스 메서드
종류	첫 번째 인자	호출 대상	용도
일반 메서드	self	인스턴스	인스턴스의 상태를 다룰 때
클래스 메서드	cls	클래스	클래스 상태나 클래스 관련 로직 처리 시

✅ @field_validator와 함께 쓰는 이유
Pydantic v2에서 @field_validator는 클래스 메서드로 작성해야 하기 때문에 @classmethod가 필요
즉, 다음과 같이 두 데코레이터를 함께 써야 함:


@field_validator('price')
@classmethod
def validate_price(cls, value):
    ...

cls: Item 클래스 자체를 의미

Pydantic이 내부적으로 클래스 컨텍스트에서 이 함수를 호출하므로, @classmethod가 반드시 필요


'''