FROM python:3-alpine

LABEL image for a very simple flask application

WORKDIR /Library

COPY . .

RUN ["pip3", "install", "pipenv"]

RUN ["pipenv", "install"]

CMD pipenv run python app.py