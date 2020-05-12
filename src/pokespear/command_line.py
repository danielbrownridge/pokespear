"""
pokespear:
Command line script to display Shakesperian descriptions of Pokémon.
"""
import argparse
import email
import sys

import pkg_resources
import pokebase
import requests

LANG = "en"
SHAKESPEARE_API_URL = (
    "https://api.funtranslations.com/translate/shakespeare.json"
)


def get_shakespearean_translation(text: str) -> str:
    """Get a Shakesperean style stranslation of some text."""
    url = SHAKESPEARE_API_URL
    data = {"text": text}
    response = requests.post(url, data=data)
    response.raise_for_status()
    json = response.json()
    translation = str(json["contents"]["translated"])
    return translation


def get_pokemon_description(pokemon: str) -> str:
    """English description of a pokemon from it's debut game apperance."""
    species = pokebase.pokemon_species(pokemon)
    entries = species.flavor_text_entries
    en_entries = filter(lambda x: x.language.name == LANG, entries)
    entry = min(en_entries, key=lambda x: x.version.id)
    description = str(entry.flavor_text)
    return description


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
