"""
Functional tests for the pokespear script.
"""
from subprocess import run


def test_script_found() -> None:
    """Check that pokespear exists and is executable."""
    args = "pokespear"
    run(args, check=True)
