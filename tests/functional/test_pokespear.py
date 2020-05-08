"""
Functional tests for the pokespear script.
"""
from subprocess import CalledProcessError, run, PIPE

import pytest


def test_script_found() -> None:
    """Check that pokespear exists and is executable."""
    args = "pokespear"
    with pytest.raises(CalledProcessError):
        run(args, check=True)


def test_no_args() -> None:
    """Check a usage message is displayed if no arguments are supplied"""
    args = "pokespear"
    with pytest.raises(CalledProcessError) as execinfo:
        run(args, check=True, encoding="utf-8", stdout=PIPE, stderr=PIPE)
    assert execinfo.value.stdout == ''
    assert execinfo.value.stderr == (
        "usage: pokespear [-h] pokemon\n"
        "pokespear: error: the following arguments are required: pokemon\n"
    )
