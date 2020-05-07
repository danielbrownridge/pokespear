"""
pokespear:
Command line script to display Shakesperian descriptions of Pokémon.
"""
from argparse import ArgumentParser
import os
import sys


def main() -> None:
    """Entry point for pokespear command line script."""
    parser = ArgumentParser(add_help=False)
    parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(os.EX_USAGE)
