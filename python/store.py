from typing import Dict
from uuid import UUID, uuid4


class NoteStore:
    """
    Класс, хранящий сообщения и взаимодействующий с ними
    """

    def __init__(self):
        self._store: Dict[UUID, str] = dict()

    def read(self, note_id: UUID):
        """
        Возвращает сообщение по идентфикатору
        :param note_id:
        :return:
        """
        try:
            return self._store.pop(note_id)
        except KeyError:
            return 'Не найдена заметка с заданным идентификатором'

    def save(self, text: str):
        """
        Сохраняет сообщение в store
        :param text:
        :return:
        """
        note_id: UUID = uuid4()
        self._store[note_id] = text
        return str(note_id)
