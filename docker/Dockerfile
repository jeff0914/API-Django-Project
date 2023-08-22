FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
RUN apt-get update && apt-get install -y gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/