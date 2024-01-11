from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient
from main import app, store
from store import NoteStore

client = TestClient(app)


def test_get_note():
    """
    Принимает текст и отдает id записки
    """
    response = client.get('/secrets/1')
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Input should be a valid UUID, invalid length: expected length 32 for simple format, found 1'

    generate_id = uuid4()
    response = client.get(f'/secrets/{generate_id}')
    assert response.status_code == 200
    assert response.json() == {
        "note_text": "Не найдена заметка с заданным идентификатором"
    }

    # Имитация заполненного хранилища
    store._store = {
        UUID("1cd3d5d6-8d72-46f0-af34-74c4cc457a9f"): "6543",
        UUID("a356397f-34a8-48ec-9f88-4ea214553795"): "332111",
        UUID("ee34ac06-3604-4f52-bf5a-09f64f6712ec"): "ttrfdd"
    }
    deleted_id = UUID("a356397f-34a8-48ec-9f88-4ea214553795")
    response = client.get(f'/secrets/{deleted_id}')
    assert response.status_code == 200
    assert response.json() == {
        'note_text': "332111"
    }


def test_post_generate_phrase(mocker):
    """
    Отдает текст записки и удаляет его
    """
    id_uuid = uuid4()
    mocker.patch(__name__ + '.NoteStore.save', return_value=str(id_uuid))
    response = client.post(
        '/generate',
        json={
            "text": "text"
        }
    )
    assert response.status_code == 201
    assert response.json() == {
        "note_id": str(id_uuid)
    }







