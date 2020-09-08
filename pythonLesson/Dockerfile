FROM python:3.8.5-slim

RUN mkdir code

COPY requirements.txt ./code

WORKDIR /code

RUN apt-get update
RUN apt-get install -y vim sqlite3
RUN pip install -U pip \
    pip install -r requirements.txt

EXPOSE 80