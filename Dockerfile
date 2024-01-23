FROM python:3.11-bookworm

VOLUME ["/var/run/docker.sock"]

# Install docker latest using their convenience script
# to minimize faff :)
RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN ./get-docker.sh

RUN /usr/local/bin/pip3 install pytest-testinfra

RUN mkdir /tests
COPY tests /tests

WORKDIR /tests
CMD /usr/local/bin/python3 -m pytest -v --show-capture=stdout
