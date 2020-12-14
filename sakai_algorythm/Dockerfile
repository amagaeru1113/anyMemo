FROM python:3.8.5

ENV PYTHONUNBUFFERED=1

RUN mkdir ./code

COPY pyproject.toml ./code
COPY poetry.lock ./code
WORKDIR /code

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get -y clean

RUN pip install -U pip \
    && pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install

EXPOSE 8080