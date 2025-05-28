from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL ='sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread': False})

'''bind : Sqlalchemy에서 Session이 어떤 DB엔진과 연결될지를 지정하는 매개변수'''
SessionLocal  = sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base = declarative_base()