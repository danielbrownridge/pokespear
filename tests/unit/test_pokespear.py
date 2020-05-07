"""
Unit tests for the pokespear script.
"""
from pokespear.command_line import main


def test_main_callable() -> None:
    """Check entry point for pokespear command-line script can be called."""
    main()
