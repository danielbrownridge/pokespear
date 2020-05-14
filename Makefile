.PHONY: install
install:
	pipenv install
.PHONY: test
test:
	pipenv run pytest
.PHONY: docker
docker:
	pipenv run docker-compose build
.PHONY: runlocal
runlocal:
	pipenv run gunicorn pokespear:app
.PHONY: run
run:
	pipenv run docker-compose up
