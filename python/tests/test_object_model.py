import pytest

from uuid import uuid4
from object_table import Notes, Base


@pytest.fixture
def note_id():
    """
    Фиксация значения идентификатора записки
    """
    return uuid4()


@pytest.fixture
def notes_cls(note_id):
    """
    Создание экземпляра записки
    """
    return Notes(id=note_id, text='text')


def test_is_instance_base(notes_cls):
    """
    Тестирование инстанса базового класса
    """
    assert isinstance(notes_cls, Base) is True


def test_check_user_table(notes_cls):
    """
    Тестирование корректности указанной таблицы
    """
    assert notes_cls.__tablename__ == 'users_notes'
