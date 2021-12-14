FROM python:3.9.6-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get clean

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-dev

COPY . ./

CMD poetry run alembic upgrade head \
    && poetry run uvicorn --host=0.0.0.0 app.main:app
