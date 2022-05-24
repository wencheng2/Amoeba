# syntax=docker/dockerfile:1
# Modified by Martin Gleeson 12/05/22

FROM python:slim-buster

EXPOSE 80/tcp

RUN apt-get update && apt-get install -y && pip install --upgrade pip && apt-get install libgl1 -y && apt-get install libglib2.0-0 -y

WORKDIR ./BasicFlaskTemplate

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV IN_DOCKER_CONTAINER Yes

COPY . .

ENTRYPOINT ["python"]

CMD ["runserver.py"]