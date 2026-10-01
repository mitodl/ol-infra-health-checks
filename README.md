# ol-infra-health-checks
A repository for MIT OL Infrastructure Health Checks

## Development

Code checks run with [prek](https://prek.j178.dev/), which reads `.pre-commit-config.yaml`. The `prek` check runs the same hooks on every pull request. When the hooks' own fixes are enough to make every hook pass, [autofix.ci](https://autofix.ci/) pushes them to the pull request as one commit. It refuses fixes to files under `.github/`, so fix those locally.

Install the version pinned as `prek-version` in `.github/workflows/autofix.yml`:

```bash
uv tool install prek==0.5.3
prek install -f              # replaces a pre-commit git hook, if one is installed
prek run --all-files
```

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
