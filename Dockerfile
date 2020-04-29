FROM python:3.7-alpine
RUN adduser -D speaker
WORKDIR /home/speaker
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
COPY app app
COPY application.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP application.py
RUN chown -R application:app ./
USER speaker
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
