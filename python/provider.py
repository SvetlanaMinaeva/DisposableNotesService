from abc import ABCMeta, abstractmethod


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


class PostgresProvider(ABCProvider):

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
