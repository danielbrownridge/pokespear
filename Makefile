.PHONY: install
install:
	pipenv install
.PHONY: test
test:
	pipenv run pytest tests
