FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

ADD blog /app

ADD appenv /app

WORKDIR /app/

RUN /bin/sh -c . "/appenv/bin/active"

RUN pip install -r requirements.txt
