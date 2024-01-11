# import uuid
# from random import choice
# from string import ascii_lowercase
#
# import pytest
#
# from store import NoteStore
#
#
# @pytest.fixture
# def store():
#     """
#     Создание экземпляра хранилища
#     """
#     return NoteStore()
#
#
# def test_read(store):
#     """
#     Возвращает сообщение по идентфикатору
#     """
#     # Генерация данных для хранилища
#     generate_id = [uuid.uuid4() for _ in range(5)]
#     generate_text = [''.join(choice(ascii_lowercase) for _ in range(20)) for _ in range(5)]
#     store._store = {key: value for key, value in zip(generate_id, generate_text)}
#     # Выбор данных для поиска
#     find_id = generate_id[3]
#     returned_message = generate_text[3]
#
#     assert store._store.get(find_id) is not None
#     assert store.read(find_id) == returned_message
#     assert store._store.get(find_id) is None
#
#
# def test_save(store):
#     """
#     Сохраняет сообщение в store
#     """
#     text = 'test1'
#     return_id = store.save(text)
#     assert isinstance(return_id, str) is True
#     assert len(store._store) == 1
#     assert store._store[uuid.UUID(return_id)] == text
