FROM python:3.9-slim-buster

ADD . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

CMD [ "python3", "pikpakTgBot.py"]
