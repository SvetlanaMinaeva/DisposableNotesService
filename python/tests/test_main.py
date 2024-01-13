from uuid import UUID, uuid4
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_get_note(mocker):
    """
    Принимает текст и отдает id записки
    """
    response = client.get('/secrets/1')
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Input should be a valid UUID, invalid length: expected length 32 for simple format, found 1'

    generate_id = uuid4()
    mocker.patch.object(main, 'read', return_value='Не найдена заметка с заданным идентификатором')
    response = client.get(f'/secrets/{generate_id}')
    assert response.status_code == 200
    assert response.json() == {
        "note_text": "Не найдена заметка с заданным идентификатором"
    }

    deleted_id = UUID("a356397f-34a8-48ec-9f88-4ea214553795")
    mocker.patch.object(main, 'read', return_value='332111')
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
    mocker.patch.object(main, 'save', return_value=str(id_uuid))
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







