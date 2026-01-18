.PHONY: clean docs test coverage-html help
.ONESHELL: release

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

clean:  ## Remove build artifacts and caches
	find . -name '*.pyc' -delete
	rm -fr build/ dist/ htmlcov/ __pycache__ .pytest_cache .ruff_cache docs/_build

docs:  ## Build documentation
	uv run sphinx-build -b html docs docs/_build/html
	@echo "Build finished. The HTML pages are in docs/_build/html."

test:  ## Run tests with pytest
	@PYTHONPATH=$(CURDIR):${PYTHONPATH} uv run pytest


coverage-html: test  ## Generate HTML coverage report
	uv run coverage html
