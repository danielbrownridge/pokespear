"""
pokespear:
Command line script to display Shakesperian descriptions of Pokémon.
"""
import argparse
import email
import sys

import pkg_resources
import pokebase


def get_pokemon_description(pokemon: str) -> str:
    """English description of a pokemon from the original game."""
    language = "en"
    version = "red"
    _ = pokemon
    species = pokebase.pokemon_species(pokemon)
    entries = species.flavor_text_entries
    entry = [entry for entry in entries
             if entry.language.name == language
             and entry.version.name == version][0]
    description = str(entry.flavor_text)
    return description


def main() -> None:
    """Entry point for pokespear command line script."""
    dist = pkg_resources.get_distribution(__package__)
    metadata = email.message_from_string(dist.get_metadata(dist.PKG_INFO))
    description = metadata["summary"]
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("pokemon")
    args = parser.parse_args()
    try:
        description = get_pokemon_description(args.pokemon)
    except ValueError as exc:
        sys.exit(str(exc))
    print(description)
