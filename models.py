'''
ORM인 SQL Alchemy가 MySQL 데이터베이스에 필요한 테이블을 만들 수 있도록 하는 것
데이터베이스를 만들고 SQL Alchemy가 우리가 만들려고 하는 이 모델과 다른 키워드를 사용하여 레코드를 저장할 수 있는
열이 있는 필요한 데이터베이스 테이블을 초기화하고 인스턴스화 한다.
'''

from sqlalchemy import Bloolean, Column, Integer, String
from database import Base


'''
# 테이블과 매핑되는 클래스 정의
'''
class User(Base):
    __tablename__ ='users'

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(50),unique =True)

class Post(Base):
    __tablename__ ='posts'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)