"""
Unit tests for the pokespear script.
"""
import pytest

from pokespear.command_line import main, get_pokemon_description


def test_main_callable():
    """Check entry point for pokespear command-line script can be called."""
    with pytest.raises(SystemExit):
        main()


@pytest.mark.parametrize("pokemon, description", [
    ("bulbasaur", (
        "A strange seed was\n"
        "planted on its\n"
        "back at birth.\f"
        "The plant sprouts\n"
        "and grows with\n"
        "this POKéMON.")),
])
def test_getpokemondescription_success(pokemon, description):
    """A text description should be returned when the name of a pokémon is
    supplied.
    """
    assert get_pokemon_description(pokemon) == description


def test_getpokemondescription_failure():
    """A ValueError should be raised if an invalid pokemon is given."""
    pokemon = "notapokemon"
    exception = "resource not found (notapokemon), check spelling"
    with pytest.raises(ValueError) as exc_info:
        get_pokemon_description(pokemon)
    assert str(exc_info.value) == exception
