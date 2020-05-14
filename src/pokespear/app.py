"""Pokespear Flask web app."""
from typing import Dict

from flask import Flask

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
    description = get_pokemon_description(name)
    translation = get_shakespearean_translation(description)
    return {
        "name": name,
        "description": translation
    }
