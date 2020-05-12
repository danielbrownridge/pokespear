"""
Unit tests for the pokespear script.
"""
import pytest
from requests.exceptions import HTTPError

from pokespear.command_line import (
    main,
    get_pokemon_description,
    get_shakespearean_translation
)


def test_main_callable():
    """Check entry point for pokespear command-line script can be called."""
    with pytest.raises(SystemExit):
        main()


@pytest.mark.parametrize("pokemon, description", [
    pytest.param("bulbasaur", (
        "A strange seed was\n"
        "planted on its\n"
        "back at birth.\f"
        "The plant sprouts\n"
        "and grows with\n"
        "this POKéMON."), id="first gen"),
    pytest.param("chikorita", (
        "A sweet aroma\n"
        "gently wafts from\n"
        "the leaf on its\f"
        "head. It is docile\n"
        "and loves to soak\n"
        "up the sun's rays."), id="second gen"),
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


@pytest.mark.xfail(raises=HTTPError, reason="Public calls ratelimited")
@pytest.mark.parametrize("text, translation", [
    ("True Layer makes Open Banking easier to use.",
     "True layer maketh ope banking easier to useth."),
])
def test_shakespearean_translation(text, translation):
    """The supplied text should be returned in Shakesperean style."""
    result = get_shakespearean_translation(text)
    assert result == translation
