FROM python:3.8.5

RUN mkdir code

COPY requirements.txt ./code

WORKDIR /code

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    vim sqlite3 \
    && apt-get -y clean


RUN apt-get update
RUN apt-get install -y vim sqlite3 python3-dev default-libmysqlclient-dev build-essential

RUN apt install -y mariadb-client

RUN pip install -U pip \
    && pip install -r requirements.txt

EXPOSE 8080