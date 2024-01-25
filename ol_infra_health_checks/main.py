from fastapi import FastAPI  # type: ignore[import-not-found]
import subprocess

healthcheck = FastAPI()


@healthcheck.get("/healthcheck/{product}")
async def root(product: str):
    # This feels dirty? But we always want flow to continue.
    test_output = None
    try:
        test_output = subprocess.run(
            ["/usr/local/bin/python3", "-m", "pytest", "-v", "--show-capture=stdout"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    except Exception:
        pass

    test_status = bool(test_output)
    return {
        "test_status": test_status,
        "test_output": test_output,
    }
