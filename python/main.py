from uuid import UUID

from fastapi import FastAPI, status, responses

from model import NoteText
from store import NoteStore

app = FastAPI()

store = NoteStore()


@app.post('/generate')
def post_generate_phrase(note: NoteText) -> responses.JSONResponse:
    """
    Принимает текст и отдает id записки
    """
    data = {
        'note_id': store.save(text=note.text)
    }
    return responses.JSONResponse(content=data, status_code=status.HTTP_201_CREATED)


@app.get('/secrets/{note_id}')
def get_note(note_id: UUID) -> responses.JSONResponse:
    """
    Отдает текст записки и удаляет его
    """
    data = {
        'note_text': store.read(note_id)
    }
    return responses.JSONResponse(content=data)
