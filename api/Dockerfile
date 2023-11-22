FROM python:3.10.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app/ /app/

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload" ]