'''(db 연동 페이지의 모듈 설명)
    sqlalchemy: DataBase와 통신하기 위한 핵심 인터페이스
        create_engine: DB연동을 위한 엔진 객체 생성
    sessionmaker: SQLAlchemy에서 세션(데이터베이스와의 단일 트랜잭션)을 생성하기 위한 팩토리
        > 여기서 세션은 쿼를 보내고 결과를 받아오는 역할을 한다.
    from sqlalchemy.ext.declarative import declarative_base: ORM에서 모델(클래스)을 정의할 때 사용할 Base 클래스를 만들기 위한 함수
        > Base 클래스를 상속받아 실제 테이블과 매핑되는 모델을 정의
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''현재 디렉토리에 있는 books.db를 SQLite db로 사용하겠다.'''
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

'''
    실제 SQLite에 접근할 수 있는 엔진 객체
    SQLite는 기본적으로 동일한 스레드에서만 DB 접근을 허용하는데, 
    이 옵션을 끄면 여러 스레드에서 같은 DB 세션을 사용할 수 있게 허용.
    >>> FastAPI 같은 비동기 프레임워크에서 사용 시 자주 설정
'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False}
)

'''engine을 바탕으로 세션을 만들 수 있는 팩토리 함수인 SessionLocal을 정의'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''모델 클래스들을 정의할 때 공통으로 상속받을 Base 클래스를 생성'''
Base = declarative_base()