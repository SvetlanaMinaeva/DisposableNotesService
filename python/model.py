from pydantic import BaseModel


class NoteText(BaseModel):
    """
    Модель сообщения
    """
    text: str
