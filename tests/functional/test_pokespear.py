"""
Functional tests for the pokespear script.
"""
from subprocess import CalledProcessError, run, PIPE

import pytest

USEAGE = "usage: pokespear [-h] pokemon\n"
POSITIONAL_ERROR = (
    "pokespear: error: the following arguments are required: pokemon\n"
)
DESCRIPTION = "Show Shakesperan description of Pokémon.\n"
POSITIONAL_ARGUMENTS = (
    "positional arguments:\n"
    "  pokemon\n"
)
OPTIONAL_ARGUMENTS = (
    "optional arguments:\n"
    "  -h, --help  show this help message and exit\n"
)


def test_script_found():
    """Check that pokespear exists and is executable."""
    args = "pokespear"
    with pytest.raises(CalledProcessError):
        run(args, check=True)


def test_no_args():
    """Check a usage message is displayed if no arguments are supplied"""
    args = "pokespear"
    with pytest.raises(CalledProcessError) as execinfo:
        run(args, check=True, encoding="utf-8", stdout=PIPE, stderr=PIPE)
    assert execinfo.value.stdout == ''
    assert execinfo.value.stderr == (
        USEAGE +
        POSITIONAL_ERROR
    )


def test_help():
    """Check that a help message is displayed when the '-h' option is used"""
    args = ["pokespear", "-h"]

    completed = run(args, check=True, encoding="utf-8", stdout=PIPE,
                    stderr=PIPE)
    assert completed.stdout == (
        USEAGE + "\n" +
        DESCRIPTION + "\n" +
        POSITIONAL_ARGUMENTS + "\n" +
        OPTIONAL_ARGUMENTS
    )
    assert completed.stderr == ''


def test_bad_pokemon():
    """Check an error message is displayed if an invalid Pokémon is given."""
    args = ["pokespear", "banana"]
    error = "resource not found (banana), check spelling\n"
    with pytest.raises(CalledProcessError) as execinfo:
        run(args, check=True, encoding="utf-8", stdout=PIPE, stderr=PIPE)
    assert execinfo.value.stdout == ""
    assert execinfo.value.stderr == error
