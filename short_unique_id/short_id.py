"""Created by Purushot on 25/11/18"""

import string
from random import randrange

__author__ = "Purushot14"

from .snowflake import Snowflake

# This original was ordered by ascii code, here `-` was 45, digits are between 48 and 57,
# upper alphabets were between 65 and 90, `_` was 95 and lower alphabets were between 97 and 122
ORIGINAL = "-" + string.digits + string.ascii_uppercase + "_" + string.ascii_lowercase

SHUFFLED = None
snowflake = Snowflake()


def _shuffle():
    """:return:"""
    source_str = ORIGINAL
    target_str = ""

    while source_str.__len__() > 0:
        r = randrange(0, source_str.__len__())
        char = source_str[r]
        target_str += char
        source_str = source_str.replace(char, "", 1)
    return target_str


def _get_shuffled():
    global SHUFFLED
    if SHUFFLED:
        return SHUFFLED
    SHUFFLED = _shuffle()
    return SHUFFLED


def _int_to_base64(num: int, is_ordered=True):
    """Converts a positive integer into a base36 string."""
    assert num >= 0
    alphabets = ORIGINAL if is_ordered else _get_shuffled()

    res = ""
    while not res or num > 0:
        num, i = divmod(num, 63)
        res = alphabets[i] + res
    return res


def get_next_snowflake_id(mult=None):
    global snowflake
    if mult:
        snowflake.set_mult(mult)
    return snowflake.__next__()


def generate_short_id(mult=None, is_ordered=True):
    _snowflake_id = get_next_snowflake_id(mult)
    return _int_to_base64(_snowflake_id, is_ordered)
