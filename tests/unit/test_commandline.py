"""
Unit tests for the pokespear script.
"""
import pytest

from pokespear.command_line import main


def test_main_callable():
    """Check entry point for pokespear command-line script can be called."""
    with pytest.raises(SystemExit):
        main()
