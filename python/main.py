from uuid import UUID

import uvicorn
from fastapi import FastAPI, status, responses

from model import NoteText
from store import read, save

app = FastAPI()


@app.post('/generate')
def post_generate_phrase(note: NoteText) -> responses.JSONResponse:
    """
    Принимает текст и отдает id записки
    """
    data = {
        'note_id': save(text=note.text)
    }
    return responses.JSONResponse(content=data, status_code=status.HTTP_201_CREATED)


@app.get('/secrets/{note_id}')
def get_note(note_id: UUID) -> responses.JSONResponse:
    """
    Отдает текст записки и удаляет его
    """
    data = {
        'note_text': read(note_id)
    }
    return responses.JSONResponse(content=data)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

