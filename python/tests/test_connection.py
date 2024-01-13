import uuid

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from config import PostgresConfig, ABCDataBaseConfig
import connection
from dev import Notes
from provider import get_provider, ABCProvider


@pytest.fixture(scope="module")
def db_connection():
    """
    Создание модели движка и сессии БД
    """
    return connection.ConnectionDataBase(
        db_config=PostgresConfig(),
        db_provider=get_provider()()
    )


@pytest.fixture(scope="module")
def session(db_connection):
    """
    Создание модели движка и сессии БД
    """
    engine = db_connection.get_engine()
    return sessionmaker(bind=engine)()


@pytest.fixture(scope="module")
def db_session(db_connection, session):
    """
    Имитация работы сессии
    """
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="module")
def new_note():
    return Notes(
        id=uuid.uuid4(),
        text='asfcsdvg'
    )


# @pytest.mark.skip(reason='DB connection')
def test_operation_method(db_connection, db_session, new_note):
    """
    Тестирование методов операций
    """
    # Создание новой записи
    connection.create(db_session, new_note)

    # Чтение созданой записи
    return_data = connection.read(db_session, Notes, id=new_note.id)
    assert len(return_data) > 0
    assert return_data[0].id == new_note.id
    assert return_data[0].text == new_note.text

    # Удаление созданной записи
    connection.delete(db_session, Notes, id=new_note.id)
    return_deleted_data = connection.read(db_session, Notes, id=new_note.id)
    assert len(return_deleted_data) == 0


def test_operation_type():
    """
    Тестирование получения метода в зависимости от операции
    """
    assert connection.operation_type.get('create') == connection.create
    assert connection.operation_type.get('read') == connection.read
    assert connection.operation_type.get('delete') == connection.delete


def test_execute(db_connection, db_session, new_note, mocker):
    """
    Выполнение запросов
    """
    func_read = mocker.patch.object(connection, 'read', return_value=new_note)
    connection.operation_type['read'] = func_read
    assert connection.execute(db_connection, 'read', Notes) == new_note
    assert func_read.assert_called_once() is None


def test_get_string():
    """
    Тестирование возвращения строки подключения db url
    """
    class DbProvider(ABCProvider):

        host: str = 'localhost'
        port: int = 5432

    class DbConfig(ABCDataBaseConfig):

        config: str = 'postgresql'
        user: str = 'test_user'
        password: str = 'test_password'
        database: str = 'postgres'

    connect = connection.ConnectionDataBase(db_config=DbConfig(), db_provider=DbProvider())

    assert connect.get_string == 'postgresql://test_user:test_password@localhost:5432/postgres'


def test_get_engine(db_connection):
    """
    Проверка возвращаемого значения метода get_engine
    Должен быть инстанс Engine
    """
    assert isinstance(db_connection.get_engine(), Engine) is True
