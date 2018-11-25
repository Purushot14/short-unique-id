# coding=utf-8
"""
    Created by prakash on 25/11/18
"""
from random import random, randrange

__author__ = 'Prakash14'

# this datetime.datetime(2018, 8, 1, 0, 0, 0, 0)
START_TIMESTAMP = 1533061800.0

ALPHABET = ''
ORIGINAL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
SHUFFLED = None
SEED = 0
PREVIOUS_SECONDS = 0


def __get_random_number(ends=1000):
    """
        return a random number based on a seed. for try to reduce the same random value
    """
    global SEED
    SEED = SEED or random()
    SEED = (SEED * 9301 + 49297) % 233280
    ran = SEED / 233280.0
    val = 0
    while ran < ends:
        ran *= 10
        if ran < ends:
            val = int(ran)
    return val


def __shuffle():
    """

    :return:
    """
    global ORIGINAL
    source_str = ORIGINAL
    target_str = ''

    while source_str.__len__() > 0:
        r = randrange(0, source_str.__len__())
        char = source_str[r]
        target_str += char
        source_str = source_str.replace(char, '', 1)
    return target_str


def __get_shuffled():
    global SHUFFLED
    if SHUFFLED:
        return SHUFFLED
    SHUFFLED = __shuffle()
    return SHUFFLED


def __int_to_base63(num: int):
    """Converts a positive integer into a base36 string."""
    assert num >= 0
    digits = __get_shuffled()

    res = ''
    while not res or num > 0:
        num, i = divmod(num, 63)
        res = digits[i] + res
    return res


def short_id(mult=1000):
    """
    this user to generate short unique_id
    this method return a short uuid this length 10 till datetime.datetime(2111, 12, 31, 0, 0, 0, 0) after that time
    size will change
    """
    global PREVIOUS_SECONDS
    from datetime import datetime
    seconds = (datetime.utcnow().timestamp() - START_TIMESTAMP) * mult
    if seconds == PREVIOUS_SECONDS:
        seconds += 1
    PREVIOUS_SECONDS = seconds
    key = __int_to_base63(int(seconds))
    prfix = __int_to_base63(__get_random_number(500000))
    while not prfix.__len__() >= 2:
        prfix = __int_to_base63(__get_random_number(500000))
    suffix_len = 2
    suffix = __int_to_base63(__get_random_number(500000))
    while not suffix.__len__() >= suffix_len:
        suffix = __int_to_base63(__get_random_number(500000))
    return prfix[-2:] + key + suffix[-suffix_len:]
