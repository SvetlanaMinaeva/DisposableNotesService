from typing import Annotated
from uuid import UUID

import uvicorn
from fastapi import FastAPI, responses, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from model import NoteText
from store import read, save

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/generate', response_class=HTMLResponse)
async def generate(request: Request) -> Jinja2Templates.TemplateResponse:
    """
    Запрос на отрисовку страницы
    """
    return templates.TemplateResponse(
        request=request, name='create_note.html'
    )


@app.post('/generate', response_model=NoteText)
async def post_generate_phrase(request: Request, note_input: Annotated[str, Form()]) -> Jinja2Templates.TemplateResponse:
    """
    Принимает текст и отдает id записки
    """
    note = NoteText(text=note_input)
    url = f'{request.base_url}secrets/{save(text=note.text)}'
    return templates.TemplateResponse(
        request=request, name='return_note_url.html', context={'url': url}
    )


@app.get('/secrets/{note_id}')
def get_note(request: Request, note_id: UUID) -> Jinja2Templates.TemplateResponse:
    """
    Отдает текст записки и удаляет его
    """
    return templates.TemplateResponse(
        request=request, name='note_read.html', context={'text': read(note_id)}
    )


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

