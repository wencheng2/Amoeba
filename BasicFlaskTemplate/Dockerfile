# syntax=docker/dockerfile:1
# Modified by Martin Gleeson 12/05/22

FROM python:latest

WORKDIR ./BasicFlaskTemplate

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV IN_DOCKER_CONTAINER Yes

COPY . .

ENTRYPOINT ["python"]

CMD ["runserver.py"]