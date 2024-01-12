from typing import Dict, Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from object_table import Base

from config import ABCDataBaseConfig
from provider import ABCProvider


class ConnectionDataBase:
    """
    Класс соединения к БД
    """

    def __init__(self, db_config: ABCDataBaseConfig, db_provider: ABCProvider):
        self.db_config = db_config
        self.db_provider = db_provider

    @property
    def get_string(self):
        """
        Возвращает строку подключения db url
        """
        return (f'{self.db_config.config}://'
                f'{self.db_config.user}:{self.db_config.password}@'
                f'{self.db_provider.host}:{self.db_provider.port}/{self.db_config.database}')

    def get_engine(self):
        """
        Возвращает движок SQLAlchemy
        """
        return create_engine(self.get_string)


def execute(db_connect: ConnectionDataBase, action_type: str, tbl_cls: Base, **kwargs):
    """
    Выполняет запросы
    """
    engine = db_connect.get_engine()

    with Session(engine) as session:
        action_method = operation_type.get(action_type, None)
        if action_method is not None:
            return action_method(session, tbl_cls, **kwargs)


def read(session: Session, tbl_cls: Base, **kwargs):
    """
    Выполняет SELECT из таблицы
    """
    statement = session.query(tbl_cls).filter_by(**kwargs)
    return statement.all()


def create(session, tbl_cls: Base):
    """
    Выполняет INSERT в таблицу
    """
    session.add(tbl_cls)
    session.commit()


def delete(session: Session, tbl_cls: Base, **kwargs):
    """
    Выполняет DELETE из таблицы
    """
    statement = session.query(tbl_cls).filter_by(**kwargs)
    statement.delete()
    session.commit()


operation_type: Dict[str, Callable] = {
    'create': create,
    'read': read,
    'delete': delete
}
