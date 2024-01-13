from os import getenv

from provider import ABCProvider, PostgresLocalhostProvider, PostgresContainerProvider, get_provider, provider_type


def test_check_abstractmethod():
    """
    Проверка начилия декоратора абстрактного метода на методах, требующих реализации
    """
    abstractmethods_config = ABCProvider.__dict__.get('__abstractmethods__')
    assert len(abstractmethods_config) == 2
    assert 'host' in abstractmethods_config
    assert 'port' in abstractmethods_config


def test_implement_postgres_providers():
    """
    Проверка соответствия атрибутов в классах-реализациях
    """
    postgres_local = PostgresLocalhostProvider()
    assert postgres_local.host == 'localhost'
    assert postgres_local.port == 5432

    postgres_container = PostgresContainerProvider()
    assert postgres_container.host == 'postgres'
    assert postgres_container.port == 5432


def test_get_provider():
    """
    Тестирование получения класса реализации
    """
    if getenv('DB_ENVIRONMENT') == 'POSTGRES_LOCAL':
        assert get_provider() == PostgresLocalhostProvider
    elif getenv('DB_ENVIRONMENT') == 'POSTGRES_CONTAINER':
        assert get_provider() == PostgresContainerProvider
    else:
        assert get_provider() is None


def test_provider_type():
    """
    Тестирование получения класса реализации
    """
    assert provider_type.keys() == {'POSTGRES_LOCAL', 'POSTGRES_CONTAINER'}
    assert provider_type.get('POSTGRES_LOCAL') == PostgresLocalhostProvider
    assert provider_type.get('POSTGRES_CONTAINER') == PostgresContainerProvider
