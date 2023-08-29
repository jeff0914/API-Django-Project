FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /code/