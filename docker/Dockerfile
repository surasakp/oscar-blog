FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

ADD blog /app

WORKDIR /app/

RUN pip install -r requirements.txt

RUN virtualenv oscar
RUN . ./oscar/bin/activate