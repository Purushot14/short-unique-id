# Python ShortId and SnowflakeId

`short_id` is a Python 3 library that provides an easy way to generate a short unique id in an orderly way using the snowflake id generation method  
* short id with ordered way
* snowflake id as ordered unique number
* short id with more unique without order

`short_id` hosted on [PyPI](http://pypi.python.org/pypi/ShortId/) and can be installed as such:


    pip install install ShortId

Alternatively, you can also get the latest source code from [Github](https://github.com/Purushot14/ShortId) and install it manually.

```python3 
import short_id
unique_id :str = short_id.generate_short_id()
snowflake_id :int = short_id.get_next_snowflake_id()

 # To increase id accuracy need to send a mult value the default value is 10000
 # and based on this mult value the id length and accuracy will change 
 unique_id :str = short_id.generate_short_id(1000000)
 snowflake_id :int = short_id.get_next_snowflake_id(1000000)
```

Development Tools
________________

### Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
poetry install

# Add new dependency
poetry add <package-name>

#Ruff
#Ruff is used for linting, auto-formatting, and import sorting:


# Install Ruff
poetry add --group dev ruff

# Run Ruff for linting and auto-fixing
poetry run ruff check . --fix

# Format code with Ruff
poetry run ruff format .
```
Running Tests

_____________

    python -m unittest discover


Changelog
__________

### Version 0.1.2

* Initial release
