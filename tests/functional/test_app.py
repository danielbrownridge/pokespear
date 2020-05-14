"""
Functional tests for the pokespear webapp.
"""


def test_service_exists(http, service_url):
    """The service should respond to an HTTP GET request."""
    assert http.get(service_url)
