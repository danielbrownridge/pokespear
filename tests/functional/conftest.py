"""Functional test fixtures for pokespear."""
import pytest
import requests
import urllib3


@pytest.fixture()
def http():
    """An http session configured to retry a few times."""
    session = requests.Session()
    return session


@pytest.fixture()
def service_url(function_scoped_container_getter):
    """The url of the service from a running container."""
    service_name = "pokespear"
    container = function_scoped_container_getter(service_name)
    url = urllib3.util.url.Url(
        scheme="http"
    )
    return url
