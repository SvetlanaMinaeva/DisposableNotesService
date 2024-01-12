FROM python:3.11

WORKDIR /usr/app/disposable_notes_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY python/ ./python

ARG POSTGRES_USER
ENV POSTGRES_USER=$POSTGRES_USER
ARG POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

CMD ["python", "./python/main.py"]