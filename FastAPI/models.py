from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float


#트랩잭션 테이블의 각 레코드에 대한 열과 데이터 유형을 만들려고 함
class Transaction(Base):
    __tablename__ = 'transactions'

    id =Column(Integer, primary_key=True, index=True)
    amount =Column(Float)
    category= Column(String)
    description= Column(String)
    is_income= Column(Boolean)
    date = Column(String)