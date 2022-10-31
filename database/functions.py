from typing import Union, Any
from sqlalchemy.orm import sessionmaker
from database.models import Data
from sqlalchemy import create_engine


class Database:
    @staticmethod
    def create_session() -> sessionmaker:
        engine = create_engine("sqlite:///Notes", echo=False, future=True)
        session = sessionmaker(bind=engine, expire_on_commit=False)
        return session

    def get_info(self) -> list[tuple]:
        database_session = self.create_session()
        with database_session() as session:
            data = session.query(Data.id, Data.site, Data.email, Data.password, Data.created_date)
            response = []
            for num, website, login, password, date in data:
                response.append((num, website, login, password, date))
            response = response[::-1]
            return response

    def add_data(self, site: str, login: str, password: str) -> Union[bool, Exception]:
        database_session = self.create_session()
        with database_session() as session:
            data = Data(
                site=site,
                email=login,
                password=password
                        )
            try:
                session.add(data)
            except Exception as ex:
                session.rollback()
                return ex
            else:
                session.commit()
                return True

    def update_data(self, num: int, site: str, login: str, password: str, create_date: str) -> Union[bool, Exception]:
        database_session = self.create_session()
        with database_session() as session:
            note = session.query(Data).filter(Data.id == num, Data.created_date == create_date).one()
            note.site = site
            note.login = login
            note.password = password
            try:
                session.add(note)
            except Exception as ex:
                session.rollback()
                raise ex
            else:
                session.commit()
                return True

    def delete_data(self, num: int, create_date: str) -> Union[bool, Exception]:
        database_session = self.create_session()
        with database_session() as session:
            note = session.query(Data).filter(Data.id == num, Data.created_date == create_date).one()
            try:
                session.delete(note)
            except Exception as ex:
                session.rollback()
                raise ex
            else:
                session.commit()
                return True
