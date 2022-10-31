from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

"Для инициализации таблицы, раскомментировать и запустить файл models.py "

class Database:
    def __init__(self):
        self.engine = create_engine("sqlite:///Notes", echo=True, future=True)

        self.Base = declarative_base()

        class Data(self.Base):
            __tablename__ = 'logins'

            id = Column(Integer, primary_key=True)
            site = Column(String)
            email = Column(String)
            password = Column(String)
            created_date = Column(String, default=str(datetime.now())[:-7])


        self.Base.metadata.create_all(self.engine)
