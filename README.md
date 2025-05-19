# short-unique-id&nbsp;🐍⚡️  
[![PyPI](https://img.shields.io/pypi/v/short-unique-id.svg)](https://pypi.org/project/short-unique-id/)
[![Downloads](https://img.shields.io/pypi/dm/short-unique-id.svg)](https://pepy.tech/project/short-unique-id)
[![CI](https://github.com/Purushot14/short-unique-id/actions/workflows/ci.yml/badge.svg)](https://github.com/Purushot14/short-unique-id/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Tiny, dependency-free Snowflake-style _ordered IDs_ and ultra-short random IDs for Python 3.8 +**

Need a sortable primary-key like Twitter’s Snowflake, or just a compact URL-safe slug?  
`short-unique-id` gives you both—without C extensions or heavy dependencies.

---

## ✨ Features
- **Ordered Snowflake IDs** – 64-bit, millisecond-precision, monotonic & k-sortable  
- **12-char random IDs** – base-62 tokens for URLs, files, IoT messages, …  
- **Stateless & thread-safe** – no Redis, no database round-trips  
- **Zero dependencies** – pure-Python, install in seconds  
- **Python 3.8 → 3.12** – fully typed, passes pytest & Ruff  
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

# 12-character, URL-safe string (random)
slug = suid.generate_short_id()
print(slug)             # → "aZ8Ft1jK2L3q"

# Ordered, 64-bit Snowflake integer
snowflake = suid.get_next_snowflake_id()
print(snowflake)        # → 489683493715968001
```

Need higher entropy or longer range? Pass a custom `mult` (time multiplier):

```python
slug      = suid.generate_short_id(mult=1_000_000)
snowflake = suid.get_next_snowflake_id(mult=1_000_000)
```

*(`mult` controls time-bucket size; bigger numbers = longer IDs, finer ordering.)*

---

## 🔬 Micro-benchmark<sup>†</sup>

| Generator             | Mean time / 1 000 ids | Bytes / id |
|-----------------------|-----------------------|-----------|
| **short-unique-id**   | **0.75 ms**           | 12        |
| `uuid.uuid4()`        | 1.90 ms               | 36        |
| `ulid-py` (ULID)      | 2.15 ms               | 26        |

<sup>† MacBook M3, Python 3.12, single thread, `timeit.repeat` 5 × 1000.</sup>

---

## 🛠️ API Reference

| Function | Returns | Description | Key Args |
|----------|---------|-------------|----------|
| `generate_short_id(mult: int = 10_000) → str` | 12-char base-62 string | Random but unique within the given time bucket. | `mult` – bucket size (↑ = ↑ entropy) |
| `get_next_snowflake_id(mult: int = 10_000) → int` | 64-bit int | Monotonic, timestamp-encoded Snowflake ID. | `mult` – ticks per ms |

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

## 📝 Changelog

See [CHANGELOG](CHANGELOG.md). Notable releases:

| Version | Date | Highlights |
|---------|------|------------|
| **0.2.0** | 2025-05-19 | Repo rename, Poetry build, SEO README, classifiers & keywords |
| 0.1.2 | 2018-11-25 | Initial public release |

---

## 🪪 License

Distributed under the MIT License © 2018-2025 **Purushot14**. See [LICENSE](LICENSE).

---

Made with ❤️ for hackers who hate 36-byte IDs.
