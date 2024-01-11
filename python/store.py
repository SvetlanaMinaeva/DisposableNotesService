﻿from uuid import UUID, uuid4

from config import PostgresConfig
from object_table import Notes
from connection import execute, Connection
from provider import PostgresProvider

db_connect = Connection(
    db_config=PostgresConfig(),
    db_provider=PostgresProvider()
)


def read(note_id: UUID) -> str:
    """
    Возвращает сообщение по идентфикатору, затем удаляет
    :param note_id:
    :return:
    """
    text = execute(db_connect, 'read', Notes, id=note_id)
    execute(db_connect, 'delete', Notes, id=note_id)
    return text[0].text if text != [] else 'Не найдена заметка с заданным идентификатором'


def save(text: str) -> str:
    """
    Сохраняет сообщение в БД
    :param text:
    :return:
    """
    note_id: UUID = uuid4()
    text = execute(db_connect, 'create', Notes(id=note_id, text=text))
    return str(note_id)
