"""Pokespear Flask web app."""
from typing import Dict

from flask import Flask

app = Flask(__name__)


@app.route("/")
def root() -> str:
    """Display the name of the service at the web root."""
    return "Pokéspear"


@app.route("/pokemon/<name>")
def pokemon(name: str) -> Dict[str, str]:
    """Shakesperean Pokémon description JSON endpoint."""

    return {
        "name": name
    }
