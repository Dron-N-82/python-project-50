install:
	uv sync

run:
	uv run gendiff files/file1.json files/file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov tests/

lint:
	uv run ruff check gendiff

check:
	test lint

build:
	uv build

.PHONY: install test lint selfcheck check build