from fastapi import FastAPI  # type: ignore[import-not-found]
import subprocess

healthcheck = FastAPI()


@healthcheck.get("/healthcheck/{product}")
async def root(product: str):
    # We need to figure out the semantics because we need both output and return code.
    test_output = subprocess.run(
        ["/usr/local/bin/python3", "-m", "pytest", "-v", "--show-capture=stdout"],
        capture_output=True,
    )
    return {
        "returnCode": test_output.returncode,
        "output": test_output.stdout.decode(""),
    }
