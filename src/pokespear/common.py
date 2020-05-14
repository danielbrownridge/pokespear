"""
pokespear:
Command line script to display Shakesperian descriptions of Pokémon.
"""
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
