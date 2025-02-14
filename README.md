# ol-infra-health-checks
A repository for MIT OL Infrastructure Health Checks

## Testing

To test this locally, simply build the docker container with:

```docker build -t "ol-infra-healthcheck" .``` in the repo's root directory. 

You can run the container with:
```docker run --name ol-infra-healthcheck ol-infra-healthcheck```

At that point you should be able to hit port 8907 on the container to access the API.

## Invoking the healthcheck API

```
curl -v http://0.0.0.0:8907/healthcheck/always_pass.py
```
