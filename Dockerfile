FROM python:3.11-bookworm

VOLUME ["/var/run/docker.sock"]

RUN apt-get -y update && apt-get -y install python3 python3-pip docker.io

RUN mkdir /tests
COPY tests /tests

WORKDIR /tests
CMD python3 -m pytest -v
