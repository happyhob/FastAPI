from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE =''

engine = create_engine(URL_DATABASE)

'''bind : Sqlalchemy에서 Session이 어떤 DB엔진과 연결될지를 지정하는 매개변수'''
SeesionLocal  = sessionmaker(autocommit = False, autoflush=False, bind = engine)