FROM python:3.7-alpine

RUN adduser -D speaker
WORKDIR /home/speaker

RUN apk update
RUN apk add --no-cache libc-dev
RUN apk add --no-cache gcc
# RUN apk add --no-cache build-essential
RUN pip install -U pip
# RUN apk add --update --no-cache py3-numpy
# ENV PYTHONPATH=/usr/lib/python3.7/site-packages

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
COPY app app
COPY app.db app.db
COPY application.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP application.py
RUN chown -R application:app ./
USER speaker
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
