from abc import ABCMeta, abstractmethod


class ABCProvider(metaclass=ABCMeta):

    @property
    @abstractmethod
    def host(self):
        pass

    @property
    @abstractmethod
    def port(self):
        pass


class PostgresProvider(ABCProvider):

    @property
    def host(self) -> str:
        return 'localhost'

    @property
    def port(self) -> int:
        return 5432
