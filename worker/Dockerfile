FROM python:3.10.12-alpine3.18

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apk update

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app/ /app/

CMD [ "celery", "-A", "tasks", "worker", "--loglevel=info", "--concurrency=1", "-E", "--logfile=/logs/celery.log" ]