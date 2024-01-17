import subprocess
import pytest
import testinfra


@pytest.fixture(scope="session")
def host(request):
    lms_id_bytes = subprocess.check_output(
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
    lms_id = str(lms_id_bytes, encoding="utf-8")
    yield testinfra.get_host(f"docker://{lms_id}")


def test_lms_has_static_assets(host):
    assert host.file("/openedx/edx-platform/lms/static/images/logo.png").exists
