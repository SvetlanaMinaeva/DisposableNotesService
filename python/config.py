from abc import ABCMeta, abstractmethod
from os import environ


class ABCConfig(metaclass=ABCMeta):

    @property
    @abstractmethod
    def config(self):
        """
        Возвращает тип конфигурации
        """
        pass

    @property
    @abstractmethod
    def user(self):
        """
        Возвращает пользователя из переменной среды
        """
        pass

    @property
    @abstractmethod
    def password(self):
        """
        Возвращает пароль пользователя из переменной среды
        """
        pass


class ABCDataBaseConfig(ABCConfig, metaclass=ABCMeta):

    @property
    @abstractmethod
    def config(self):
        """
        Возвращает тип конфигурации
        """
        pass


    @property
    @abstractmethod
    def user(self):
        """
        Возвращает пользователя из переменной среды
        """
        pass

    @property
    @abstractmethod
    def password(self):
        """
        Возвращает пароль пользователя из переменной среды
        """
        pass

    @property
    @abstractmethod
    def database(self):
        """
        Установка используемой БД
        """
        pass


class PostgresConfig(ABCDataBaseConfig):

    @property
    def user(self) -> str:
        """
        Возвращает пользователя из переменной среды
        """
        return environ.get('POSTGRES_USER')

    @property
    def password(self) -> str:
        """
        Возвращает пароль пользователя из переменной среды
        """
        return environ.get('POSTGRES_PASSWORD')

    @property
    def database(self) -> str:
        """
        Установка используемой БД
        :return:
        """
        return 'notes'

    @property
    def config(self):
        """
        Возвращает тип конфигурации
        """
        return 'postgresql'
