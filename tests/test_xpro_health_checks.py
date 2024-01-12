import subprocess
import pytest
import testinfra


@pytest.fixture(scope="session")
def host(request):
    lms_id = subprocess.check_output(
        [
            "docker",
            "compose",
            "-f",
            "/etc/docker/compose/docker-compose.yaml",
            "ps",
            "-q",
            "lms",
        ]
    ).strip()
    yield testinfra.get_host(f"docker://{lms_id}")


def test_lms_is_running(host):
    assert host.file("/edx-platform/lms/static/images/logo.png").exists
