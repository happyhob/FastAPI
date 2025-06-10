from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base     


SQLALCHEMY_DATABASE_URL ='sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread': False})

'''bind : Sqlalchemy에서 Session이 어떤 DB엔진과 연결될지를 지정하는 매개변수'''
SessionLocal  = sessionmaker(autocommit = False, autoflush=False, bind = engine)


#ORM(객체-관계 매핑)을 사용할 때 모든 모델 클래스의 부모(Base 클래스)를 생성하는 함수
#Base는 모든 SQLAlchemy 모델 클래스가 상속받아야 하는 기본 클래스
#이 Base를 상속받은 클래스는 SQLAlchemy에게 "이 클래스는 데이터베이스 테이블과 매핑되는 ORM 모델입니다"라고 알려주는 역할
Base = declarative_base()


'''
| 요소                   | 설명                                    |
| -------------------- | ------------------------------------- |
| `declarative_base()` | SQLAlchemy 모델들의 부모 클래스 생성             |
| `Base`               | 모델 정의 시 상속해야 하는 클래스                   |
| `Base.metadata`      | 모든 모델의 테이블 메타데이터가 모여 있음               |
| `Base.metadata.create_all()` | 실제 DB에 테이블을 만드는 명령      |
| 목적                   | Python 클래스를 DB 테이블처럼 사용할 수 있게 함 (ORM) |

'''