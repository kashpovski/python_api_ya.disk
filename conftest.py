import pytest


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'y0_AgAAAABoUSZVAADLWwAAAADbQFyZ_tnuCKbVSfOiuj03HPYWz4sl7bQ'

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default=URL,
        help="This is request url"
    )
    parser.addoption(
        "--token",
        default=TOKEN,
        help="This is token"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def token(request):
    return request.config.getoption("--token")
