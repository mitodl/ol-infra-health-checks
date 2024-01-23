FROM python:3.11-bookworm

VOLUME ["/var/run/docker.sock"]

# Add Docker's official GPG key:
RUN apt-get -y update
RUN apt-get -y install ca-certificates curl gnupg
RUN install -m 0755 -d /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get -y update

# Actually install docker & docker compose
RUN apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install pytest & testinfra
RUN /usr/local/bin/pip3 install pytest-testinfra

RUN mkdir /tests
COPY tests /tests

WORKDIR /tests
CMD /usr/local/bin/python3 -m pytest -v --show-capture=stdout
