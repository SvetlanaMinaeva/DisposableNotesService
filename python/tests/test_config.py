from os import environ

import pytest

from config import PostgresConfig


@pytest.fixture
def connect():
    """
    Создается экземпляр класса PostgresConfig
    """
    return PostgresConfig()


def test_get_user(connect):
    """
    Тестирование возвращения атрибута user
    """
    if environ.get('POSTGRES_USER') is None:
        assert connect.user is None
    else:
        assert connect.user == environ.get('POSTGRES_USER')


def test_get_password(connect):
    """
    Тестирование возвращения атрибута password
    """
    if environ.get('POSTGRES_PASSWORD') is None:
        assert connect.password is None
    else:
        assert connect.password == environ.get('POSTGRES_PASSWORD')


def test_database(connect):
    """
    Тестирование возвращения атрибута database
    """
    assert connect.database == 'notes'


def test_get_config(connect):
    """
    Тестирование возвращения атрибута config
    """
    assert connect.config == 'postgresql'

