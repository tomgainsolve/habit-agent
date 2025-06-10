#!/bin/bash

# Format Python code
poetry run black .
poetry run isort .

# Type checking
poetry run mypy . 