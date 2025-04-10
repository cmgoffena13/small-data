lint:
	uv run -- ruff check --fix

format:
	uv run -- ruff format

test:
	uv run -- pytest -v -n auto

install:
	uv sync --frozen --compile-bytecode

clean:
	rm -rf __pycache__ logs .pytest_cache .ruff_cache
	uv venv --python 3.12