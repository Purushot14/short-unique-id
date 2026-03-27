# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`short-unique-id` — a zero-dependency Python library (3.9+) for Snowflake-style ordered 64-bit IDs and 12-char base-62 random IDs. Uses Poetry for dependency management.

## Commands

```bash
# Install dependencies
poetry install

# Run all tests with coverage (CI threshold: 90%)
pytest -q --cov=short_unique_id --cov-report=term --cov-fail-under=90

# Run a single test
pytest tests/test_snowflake.py::TestSnowflake::test_get_next_id -v

# Lint
ruff check .

# Format
ruff format .

# Lint with auto-fix (also what pre-commit runs)
ruff check . --fix
```

## Architecture

Two modules under `short_unique_id/`:

- **`snowflake.py`** — Core Snowflake ID generator. 64-bit IDs composed of timestamp (custom epoch 2020-01-01), 16-bit machine ID (from IP/UUID), 8-bit process ID, and 5-bit sequence counter. Thread-safe via `threading.Lock`. The `Snowflake` class supports iterator protocol and a `mult` parameter controlling time precision.

- **`short_id.py`** — Wraps Snowflake output with base-62 encoding using two alphabets: `ORIGINAL` (ASCII-ordered, for lexicographic sorting) and `SHUFFLED` (randomized). `generate_short_id()` produces ~12-char strings; `get_next_snowflake_id()` returns raw integers.

- **`__init__.py`** — Public API exports: `generate_short_id` and `get_next_snowflake_id`.

## Code Style

- Ruff for linting and formatting (configured in `pyproject.toml`)
- Line length: 120
- Target: Python 3.9
- Double quotes
- Rule sets: E, F, B, I, UP, N, C