FROM python:3.11-bookworm

VOLUME ["/var/run/docker.sock"]

RUN apt-get -y update && apt-get -y install docker.io
RUN /usr/local/bin/pip3 install pytest-testinfra

RUN mkdir /tests
COPY tests /tests

WORKDIR /tests
ENTRYPOINT ['/usr/local/bin/python3' '-m pytest' '-v' '--show-capture=stdout']
