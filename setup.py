# coding=utf-8
"""
    Created by Purushot on 25/11/18
"""

__author__ = 'Purushot14'
__version__ = "0.1.2"
__name__ = "short-unique-id"

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__name__,  # This is the name of the package
    version=__version__,
    author=__author__,  # Full name of the author
    author_email="prakash.purushoth@gmail.com",
    description="Short id generator",
    long_description=long_description,  # Long description read from the the readme file
    keywords=["short", "id", "uuid", "shortid", "SnowflakeId", "short uuid", "tinyid", "unique id"],
    long_description_content_type="text/markdown",
    packages=["short_id"],  # List of all python modules to be installed
    py_modules=["short_id"],
    url="https://github.com/Purushot14/ShortId",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Code Generators"
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.6',  # Minimum version requirement of the package
    install_requires=[]  # Install other dependencies if any
)
