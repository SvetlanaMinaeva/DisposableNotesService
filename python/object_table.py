from sqlalchemy import Column, Text, UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Notes(Base):
    """
    Объект таблицы users_notes
    """
    __tablename__ = 'users_notes'

    id = Column(UUID, primary_key=True, index=True)
    text = Column(Text)
