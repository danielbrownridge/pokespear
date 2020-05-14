"""
pokespear:
Command line script to display Shakesperian descriptions of Pokémon.
"""
import argparse
import email
import sys

import pkg_resources
import requests

from . import get_pokemon_description, get_shakespearean_translation

LANG = "en"
SHAKESPEARE_API_URL = (
    "https://api.funtranslations.com/translate/shakespeare.json"
)


def main() -> None:
    """Entry point for pokespear command line script."""
    dist = pkg_resources.get_distribution(__package__)
    metadata = email.message_from_string(dist.get_metadata(dist.PKG_INFO))
    description = metadata["summary"]
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("pokemon", help="The name of a Pokémon e.g. bulbasaur")
    args = parser.parse_args()
    try:
        description = get_pokemon_description(args.pokemon)
    except ValueError as exc:
        sys.exit(str(exc))
    try:
        translation = get_shakespearean_translation(description)
    except requests.exceptions.HTTPError as exc:
        sys.exit(str(exc))
    print(translation)
