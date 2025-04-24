'''
nosql db는 이것을 json으로 보내지만 우리의 python이 이것을 객체로 사용하기 어려울 것이다.
우리는 이 정보를 우리의 애플리케이션 내에서 사용할 수 있는 것으로 역직렬화하거나 직렬화 할 수 있어야 한다.

그래서 우리는 schema패키지 안에 새로운 스키마를 생성하고 싶다.

'''

'''
schemas.py
1. 개별 직렬화를 만드는 것
    우리는 할 일 객체 사전에 연결하는 것, 각 항목의 ID와 KEY를 볼 것이다.

우리가 하고 싶은 것은 모든 것을 검색하는 것이다.
현재 이것은 단지 하나의 항목을 역직렬화하는 것임.

모든 할 일을 반환할 때도
'''


def individual_serial(todo)-> dict:
    return {
        "id": str(todo["_id"]),      # '_' 이건 MongoDB가 열을 찾는 특정 방식이다.
        "name" : todo["name"],
        "description": todo["description"],
        "complate":todo["complate"]
    }


def list_serial(todos) ->list:
    return [individual_serial(todo) for todo in todos]