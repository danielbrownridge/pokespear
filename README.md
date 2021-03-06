# pokespear

## Dependencies

 * [Python 3 (3.6+)](https://docs.python.org/3.6/using/index.html)
 * [Docker](https://docs.docker.com/engine/install/)
 * [GNU Make](https://www.gnu.org/software/make/)

## Installation

By default make will use pipenv to create a virtualenv and install pokespear
as command line took implemented as a user executable python package.

    $ make install

## Build the Docker container

The container uses docker compose which is installed via pipenv so run
`make install` first.

    $ make install
    $ make docker

## Run the webapp

The web app can either be run directly or via the container:

### locally

    $ make runlocal

The app will come up on http://localhost:8000

### in a docker container

    $ make run

The app will come up on http://localhost/

## Command line usage

    $ pipenv shell
    (pokespear) $ pokespear -h
    usage: pokespear [-h] pokemon

    Show Shakesperan description of Pokémon.

    positional arguments:
      pokemon     The name of a Pokémon e.g. bulbasaur

    optional arguments:
      -h, --help  show this help message and exit
    
    (pokespear) $ pokespear bulbasaur
    A strange seed wast planted on its back at birth. The plant sprouts and grows with this pokémon. 

## Tests

The tests run the docker containers so may take a moment to complete:

    $ make test


## Continuous integration

The tests are running in Travis CI https://travis-ci.com/github/danielbrownridge/pokespear
