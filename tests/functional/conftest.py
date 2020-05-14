"""Functional test fixtures for pokespear."""
import pytest
import requests
import urllib3
from urllib3.util.retry import Retry
from http import HTTPStatus

@pytest.fixture()
def http():
    """An http session configured to retry a few times."""
    session = requests.Session()
    prefix = "http://"
    forcelist = {
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.NOT_IMPLEMENTED,
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT
    }
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=forcelist)
    adapter = requests.adapters.HTTPAdapter(max_retries=retries)
    session.mount(prefix, adapter)
    return session


@pytest.fixture()
def service_url(function_scoped_container_getter):
    """The url of the service from a running container."""
    service_name = "pokespear"
    container = function_scoped_container_getter.get(service_name)
    network_info = container.network_info[0]
    url = urllib3.util.url.Url(
        scheme="http",
        host=network_info.hostname,
        port=network_info.host_port
    )
    return url
