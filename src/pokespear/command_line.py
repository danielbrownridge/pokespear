"""
pokespear:
Command line script to display Shakesperian descriptions of Pokémon.
"""
import argparse
import email
import pkg_resources


def main() -> None:
    """Entry point for pokespear command line script."""
    dist = pkg_resources.get_distribution(__package__)
    metadata = email.message_from_string(dist.get_metadata(dist.PKG_INFO))
    description = metadata["summary"]
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("pokemon")
    parser.parse_args()
