from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# "Для инициализации таблицы, раскомментировать и запустить файл models.py "
# engine = create_engine("sqlite:///Notes", echo=True, future=True)

Base = declarative_base()


class Data(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    site = Column(String)
    email = Column(String)
    password = Column(String)
    created_date = Column(String, default=str(datetime.now())[:-7])


# Base.metadata.create_all(engine)
