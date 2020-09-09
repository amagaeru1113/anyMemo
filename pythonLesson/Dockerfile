FROM python:3.8.5-slim

RUN mkdir code

COPY requirements.txt ./code

WORKDIR /code

RUN apt-get update \
    apt-get install -y vim sqlite3 python3-dev default-libmysqlclient-dev build-essential

RUN apt install -y mariadb-client

RUN pip install -U pip \
    pip install -r requirements.txt

EXPOSE 80