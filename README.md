# short-unique-id&nbsp;🐍⚡️

[![PyPI](https://img.shields.io/pypi/v/short-unique-id.svg)](https://pypi.org/project/short-unique-id/)
[![Downloads](https://img.shields.io/pypi/dm/short-unique-id.svg)](https://pepy.tech/project/short-unique-id)
[![CI](https://github.com/Purushot14/short-unique-id/actions/workflows/ci.yml/badge.svg)](https://github.com/Purushot14/short-unique-id/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/short-unique-id.svg)](https://pypi.org/project/short-unique-id/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/short-unique-id.svg)](https://pypi.org/project/short-unique-id/#files)
[![Lines of Code](https://sloc.xyz/github/Purushot14/short-unique-id)](https://github.com/Purushot14/short-unique-id)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-blueviolet)](https://docs.astral.sh/ruff/)
[![Coverage](https://img.shields.io/codecov/c/github/Purushot14/short-unique-id/main.svg?logo=codecov)](https://app.codecov.io/gh/Purushot14/short-unique-id)
[![GitHub Release Date](https://img.shields.io/github/release-date/Purushot14/short-unique-id.svg)](https://github.com/Purushot14/short-unique-id/releases)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Purushot14/short-unique-id/pulls)
[![CodeQL](https://github.com/Purushot14/short-unique-id/actions/workflows/codeql.yml/badge.svg)](https://github.com/Purushot14/short-unique-id/security/code-scanning)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

> **Tiny, dependency-free Snowflake-style _ordered IDs_ and ultra-short unique IDs for Python 3.9+**

Need a sortable primary-key like Twitter’s Snowflake, or just a compact URL-safe slug?
`short-unique-id` gives you both—without C extensions or heavy dependencies.

---

## ✨ Features
- **Ordered Snowflake IDs** – 64-bit, monotonic & k-sortable (100 μs precision at default `mult`)
- **Short base-64 string IDs** – compact, URL-safe tokens for URLs, files, IoT messages, …
- **Sortable or shuffled** – ordered alphabet for lexicographic sort, or shuffled alphabet for opaque tokens
- **Stateless & thread-safe** – no Redis, no database round-trips
- **Zero dependencies** – pure-Python, install in seconds
- **Python 3.9 → 3.14** – fully typed, passes pytest & Ruff
- **MIT licensed**

---

## 🚀 Install

```bash
pip install short-unique-id
```

Or grab the latest dev build:

```bash
pip install git+https://github.com/Purushot14/short-unique-id.git
```

---

## ⚡ Quick-start

```python
import short_unique_id as suid

# URL-safe, lexicographically sortable string (default is_ordered=True)
slug = suid.generate_short_id()
print(slug)             # → "1vAo4-1g-1---"

# Opaque token using shuffled alphabet
token = suid.generate_short_id(is_ordered=False)
print(token)            # → "qZ8Ft1jK2L3R"

# Ordered, 64-bit Snowflake integer
snowflake = suid.get_next_snowflake_id()
print(snowflake)        # → 489683493715968001
```

Need higher precision or longer range? Pass a custom `mult` (ticks per second):

```python
slug      = suid.generate_short_id(mult=1_000_000)
snowflake = suid.get_next_snowflake_id(mult=1_000_000)
```

---

## 🔬 Micro-benchmark<sup>†</sup>

| Generator             | Mean time / 1 000 ids | Bytes / id |
|-----------------------|-----------------------|-----------|
| **short-unique-id**   | **0.75 ms**           | ~11–13    |
| `uuid.uuid4()`        | 1.90 ms               | 36        |
| `ulid-py` (ULID)      | 2.15 ms               | 26        |

<sup>† MacBook M3, Python 3.13, single thread, `timeit.repeat` 5 × 1000.</sup>

---

## 🛠️ API Reference

| Function | Returns | Description | Key Args |
|----------|---------|-------------|----------|
| `generate_short_id(mult=None, is_ordered=True) → str` | base‑64 string | Snowflake ID encoded as a compact string. Sortable by default; pass `is_ordered=False` for an opaque token. | `mult` – ticks per second (default 10 000); `is_ordered` – use ASCII-ordered alphabet |
| `get_next_snowflake_id(mult=None) → int` | 64-bit int | Monotonic, timestamp‑encoded Snowflake ID. | `mult` – ticks per second (default 10 000) |

---

## 📚 When to use it

* Primary keys in distributed databases (fits in `BIGINT`)  
* Short share links or invite codes  
* File/folder names on S3 / GCS (lexicographic sort ≈ creation time)  
* Message IDs in event streams & IoT payloads  
* Anywhere you’d reach for UUIDs but want **shorter or ordered** IDs

---

## 🤝 Contributing

1. `git clone https://github.com/Purushot14/short-unique-id && cd short-unique-id`  
2. `poetry install` – sets up venv & dev tools  
3. `poetry run pytest` – all green? start hacking!  
4. Run `ruff check . --fix && ruff format .` before PRs  
5. Open a PR – stars and issues welcome ⭐

---

## 🛡️ Pre-commit (via Poetry)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

Make sure you’ve added **pre-commit** as a dev dependency:

```bash
poetry add --dev pre-commit
```

Set up the Git hook and run it against all files:

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files
```

---

## 📝 Changelog

Notable releases:

| Version   | Date       | Highlights                                                  |
|-----------|------------|-------------------------------------------------------------|
| **0.2.1** | 2025-05-20 | Python3.13 support added and Badges added on readme         |
| **0.2.0** | 2025-05-19 | Repo rename, Poetry build, SEO README, classifiers & keywords |
| 0.1.2     | 2018-11-25 | Initial public release                                      |

---

## 🪪 License

Distributed under the MIT License © 2018–2025 **Purushot14**. See [LICENSE](LICENSE).

---

Made with ❤️ for hackers who hate 36‑byte IDs.
