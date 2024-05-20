FROM python:3.10-slim-bullseye

ENV POETRY_HOME=/opt/poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN python3 -m venv $POETRY_HOME \
    && $POETRY_HOME/bin/pip install poetry==1.8.2 

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY *.py ./
COPY mco/ mco/

ENTRYPOINT [ "poetry", "run", "python", "app.py" ]
