FROM python:3.11-bookworm

VOLUME ["/var/run/docker.sock"]

RUN apt-get -y update && apt-get -y install python3 python3-pip docker.io python3-testinfra

RUN mkdir /tests
COPY tests /tests

WORKDIR /tests
# ENTRYPOINT /usr/bin/python3 -m pytest -v --show-capture=stdout
