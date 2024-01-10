import pytest
from pydantic import ValidationError

from model import NoteText


def test_note_text():
    """
    Тестирование модели заметки
    """
    # На вход поданы валидные данные - строка
    new_message = NoteText(
        text='This is test'
    )
    assert new_message.text == 'This is test'

    # На вход поданы невалидные данные - integer
    with pytest.raises(ValidationError):
        NoteText(text=122421)

