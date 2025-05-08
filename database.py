from sqlalchemy import create_engine    #데이터베이스가 애플리케이션과 통신할 수 있는 엔진을 만든다.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base     #선형적 데이터베이스를 가져올려고한다

'''
SQLAlchemy에서 사용하는 ORM(Object Relational Mapping) 기능 중 하나로, 
데이터베이스 테이블과 매핑되는 파이썬 클래스의 베이스(기초)가 되는 클래스를 생성할 때 사용됩니다.


'''

URL_DATABASE ='mysql+pymysql://root:test1234!@localhost:3306/BlogApplication'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


'''
declarative_base()는 클래스 기반 ORM 모델 정의를 할 수 있도록 **베이스 클래스(Base class)**를 만들어 줌
이 베이스 클래스를 상속받아 정의한 각 클래스는 데이터베이스의 테이블과 연결
'''
Base = declarative_base()