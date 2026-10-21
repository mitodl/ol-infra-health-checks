FROM python:3.13-bookworm@sha256:073ffebb96ae4d0ed73ccad59f08c47bd84af8a79f5258130f8458ac50ad9ff4

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
RUN /usr/local/bin/pip3 install pytest-testinfra fastapi[all]

# Install dagster & dagster_graphql
RUN /usr/local/bin/pip3 install dagster dagster_graphql

RUN mkdir /healthcheck_api
COPY healthcheck_api /healthcheck_api
RUN mkdir /tests
COPY tests /tests

WORKDIR /healthcheck_api
CMD ["uvicorn", "main:healthcheck", "--host", "0.0.0.0", "--port", "8907", "--proxy-headers","--log-level","trace"]
