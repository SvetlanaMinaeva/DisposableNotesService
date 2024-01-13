from uuid import uuid4
from cryptography.fernet import Fernet

import store
from connection import ConnectionDataBase
from object_table import Notes


def test_check_variables():
    """
    Проверка содержимого переменной на корректность
    """
    assert isinstance(store.db_connect, ConnectionDataBase) is True
    assert isinstance(store.fernet_obj, Fernet) is True


def test_read(mocker):
    """
    Возвращает сообщение по идентфикатору
    """
    # Генерация данных для хранилища
    note = Notes(id=uuid4(), text=store.fernet_obj.encrypt('Return text'.encode()).decode())
    mocker.patch.object(store, 'execute', side_effect=[[note], None])
    assert store.read(note_id=note.id) == 'Return text'


def test_save(mocker):
    """
    Сохраняет сообщение в store
    """
    text = 'test1'
    mocker.patch.object(store, 'execute', return_value='test1')
    return_id = store.save(text)
    assert isinstance(return_id, str) is True

