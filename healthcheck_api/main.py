from fastapi import FastAPI, Response, status# type: ignore[import-not-found]
import subprocess

healthcheck = FastAPI()


@healthcheck.get("/healthcheck/{test_name}", status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
async def root(test_name: str, response: Response):
    test_result = subprocess.run(
        [
            "/usr/local/bin/python3",
            "-m",
            "pytest",
            "-vv",
            "--show-capture=stdout",
            f"{test_name or ''}",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd="/tests",
    )

    test_returncode = test_result.returncode
    test_passed = not test_returncode
    test_output = test_result.stdout

    if test_passed:
        response.status_code = status.HTTP_200_OK

    return {
        "test_status": test_passed,
        "test_output": test_output,
    }
