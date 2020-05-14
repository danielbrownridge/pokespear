"""
Functional tests for the pokespear webapp.
"""
from urllib.parse import urljoin



def test_service_exists(http, service_url):
    """The service should respond to an HTTP GET request."""
    assert http.get(service_url)


def test_pokemon_endpoint(http, service_url):
    """The pokemon endpoint should return a JSON dictionary with the fields
     - 'name': the name of the pokemon
     - 'description' the description translated into Shakespearean style
    """
    service_url = "http://localhost:5000"
    endpoint = "pokemon"
    pokemon = "bulbasaur"
    path = f"{endpoint}/{pokemon}"
    description = (
        "A strange seed wast planted on its back at birth. The plant sprouts a"
        "nd grows with this pokémon."
    )
    json = {
        "name": pokemon,
        "description": description
    }
    url = urljoin(service_url, path)
    response = http.get(url)
    print(json)
    assert response.json() == json
