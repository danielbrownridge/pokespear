"""Pokespear Flask web app."""
from typing import Dict

from flask import Flask
from requests.exceptions import HTTPError

from .common import get_pokemon_description, get_shakespearean_translation

app = Flask(__name__)
app.debug = True


@app.route("/")
def root() -> str:
    """Display the name of the service at the web root."""
    return "Pokéspear"


@app.route("/pokemon/<name>")
def pokemon(name: str) -> Dict[str, str]:
    """Shakesperean Pokémon description JSON endpoint."""
    response = {
        "name": name
    }
    try:
        description = get_pokemon_description(name)
    except ValueError as exc:
        response["error"] = str(exc)
    try:
        response["description"] = get_shakespearean_translation(description)
    except HTTPError as exc:
        response["error"] = str(exc)
    return response
