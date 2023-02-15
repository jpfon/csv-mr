FROM python:3.11.2-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

ARG POETRY_VERSION="1.3.2"
RUN python -m pip install --upgrade pip poetry==${POETRY_VERSION}

WORKDIR /app
COPY poetry.toml pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . ./
