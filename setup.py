"""
short-unique-id
Tiny, dependency-free Snowflake-style and random short-UUID generator for Python.
"""

from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).resolve().parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    # ---- Core metadata ----------------------------------------------------
    name="short-unique-id",  # PyPI project name
    version="0.2.0",  # bump every release
    author="Purushot14",
    author_email="prakash.purushot@gmail.com",
    description="Tiny, dependency-free Snowflake-style and random short ID generator for Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    # ---- URLs -------------------------------------------------------------
    url="https://github.com/Purushot14/short-unique-id",
    project_urls={
        "Documentation": "https://github.com/Purushot14/short-unique-id#readme",
        "Source": "https://github.com/Purushot14/short-unique-id",
        "Issue Tracker": "https://github.com/Purushot14/short-unique-id/issues",
    },
    # ---- Search / filter helpers -----------------------------------------
    keywords=[
        "shortid",
        "short-id",
        "snowflake",
        "uuid",
        "unique-id",
        "identifier",
        "id-generator",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    # ---- Packaging options -----------------------------------------------
    packages=find_packages(include=["short_unique_id", "short_unique_id.*"]),
    python_requires=">=3.8",
    install_requires=[],  # add runtime deps here if ever needed
    include_package_data=True,  # include files tracked by MANIFEST.in
    zip_safe=False,
)
