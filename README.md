# pokespear

## Dependencies

 * [Python 3 (3.6+)](https://docs.python.org/3.6/using/index.html)
 * [pipenv](https://github.com/pypa/pipenv#installation)
 * [Docker](https://docs.docker.com/engine/install/)
 * [GNU Make](https://www.gnu.org/software/make/)

## Installation

By default make will use pipenv to create a virtualenv and install pokespear
as a user executable python package.

    $ make install

## Usage

    $ pipenv run pokespear
    $ pipenv run pokespear -h
    usage: pokespear [-h] pokemon

    Show Shakesperan description of Pokémon.

    positional arguments:
      pokemon     The name of a Pokémon e.g. bulbasaur

    optional arguments:
      -h, --help  show this help message and exit
