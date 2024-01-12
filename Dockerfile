FROM python:3.11

WORKDIR /usr/app/disposable_notes_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY python/ ./python

CMD ["python", "./python/main.py"]