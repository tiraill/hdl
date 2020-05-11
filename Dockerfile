FROM python:3.7-alpine3.10

WORKDIR /src

ENV TZ 'UTC'
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache libpq tzdata libffi git \
    && pip install --no-cache-dir -U pip==19.1.1 setuptools==41.2.0 setuptools-scm==3.3.3

COPY requirements requirements

RUN cat requirements/apk.txt | xargs apk add --no-cache \
    && cat requirements/apk_build.txt | xargs apk add --no-cache --virtual .build-deps \
    && pip install --no-cache-dir -r requirements/python.txt \
    && apk del --no-cache .build-deps

COPY ./src /src