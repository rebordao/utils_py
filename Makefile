all: flake8 mypy test-fixtures test-full

flake8:
	@flake8 --exclude=./venv .
.PHONY: flake8

mypy:
	@mypy utils_py
.PHONY: mypy

test-full:
	@python -m pytest -v tests/
.PHONY: test-full
