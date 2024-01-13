from os import environ

import pytest

from config import PostgresConfig, ABCConfig, ABCDataBaseConfig


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


def test_check_abstractmethod():
    """
    Проверка начилия декоратора абстрактного метода на методах, требующих реализации
    """
    abstractmethods_config = ABCConfig.__dict__.get('__abstractmethods__')
    assert len(abstractmethods_config) == 3
    assert 'user' in abstractmethods_config
    assert 'password' in abstractmethods_config
    assert 'config' in abstractmethods_config

    abstractmethods_config_db = ABCDataBaseConfig.__dict__.get('__abstractmethods__')
    assert len(abstractmethods_config_db) == 4
    assert 'user' in abstractmethods_config_db
    assert 'password' in abstractmethods_config_db
    assert 'config' in abstractmethods_config_db
    assert 'database' in abstractmethods_config_db