from abc import ABCMeta, abstractmethod
from os import getenv


class ABCProvider(metaclass=ABCMeta):

    @property
    @abstractmethod
    def host(self) -> str:
        """
        Возвращает название хоста
        """
        pass

    @property
    @abstractmethod
    def port(self) -> int:
        """
        Возвращает порт
        """
        pass


class PostgresContainerProvider(ABCProvider):

    @property
    def host(self) -> str:
        """
        Возвращает название хоста
        """
        return 'postgres'

    @property
    def port(self) -> int:
        """
        Возвращает порт
        """
        return 5432


class PostgresLocalhostProvider(ABCProvider):

    @property
    def host(self) -> str:
        """
        Возвращает название хоста
        """
        return 'localhost'

    @property
    def port(self) -> int:
        """
        Возвращает порт
        """
        return 5432


def get_provider():
    """
    Возвращает провайдер в зависимости от среды запуска БД
    """
    return provider_type.get(getenv('DB_ENVIRONMENT'))


provider_type = {
    'POSTGRES_LOCAL': PostgresLocalhostProvider,
    'POSTGRES_CONTAINER': PostgresContainerProvider
}
