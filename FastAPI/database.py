from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'sqlite:///./finance.db'

engine = create_engine(URL_DATABASE, connect_args={"check_same_thread":False})

'''옵션 설명
flush: DB에 변경 내용을 보냄 → 하지만 아직 커밋되지 않음 (롤백 가능)

commit: 변경 내용을 영구 저장
'''
SessionLocal = sessionmaker(autocommit =False, autoflush=False, bind= engine)

Base = declarative_base()

