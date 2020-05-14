"""Module configuration for the Pokéspear app."""
from .app import app
from .common import get_shakespearean_translation, get_pokemon_description

__all__ = [
    "app",
    "get_shakespearean_translation",
    "get_pokemon_description"
]
