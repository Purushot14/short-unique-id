"""
    Created by Purushot at 30/11/22
"""
__author__ = 'Purushot14'

import ipaddress
import logging
import os
import time
import uuid
from _socket import gaierror
from socket import gethostbyname, gethostname

# Wednesday, 1 January 2020 00:00:00 GMT
from threading import Lock

start_epoch = 1577817000
machine_id_bits = 16
process_id_bits = 8
sequence_bits = 5
machine_id_mask = -1 ^ (-1 << machine_id_bits)
process_id_mask = -1 ^ (-1 << process_id_bits)
sequence_mask = -1 ^ (-1 << sequence_bits)
timestamp_left_shift = sequence_bits + process_id_bits + machine_id_bits


def get_machine_id(ip_address: str = None, is_retry=False):
    try:
        ip_address = ip_address or gethostbyname(gethostname() or "localhost")
    except gaierror:
        if is_retry:
            return uuid.getnode() & machine_id_mask
        return get_machine_id(is_retry=True)
    return int(ipaddress.ip_address(ip_address)) & machine_id_mask


def get_process_id():
    return os.getpid() & process_id_mask


def get_worker_id():
    return get_machine_id() | get_process_id()


class Snowflake:

    def __init__(self, worker_id=None, mult=10000):
        logging.info(f"Snowflake init called")
        self.worker_id = worker_id or get_worker_id()
        self._mult = mult
        self.__last_timestamp = -1
        self.__sequence = 0
        self._lock = Lock()

    def set_mult(self, mult):
        self._mult = mult
        time.sleep(1/mult)

    @property
    def start_epoch(self): return start_epoch * self._mult

    @property
    def current_time(self) -> int: return int(self._mult * time.time())

    def _next_id(self):
        current_time = self.current_time
        if self.__last_timestamp == current_time:
            self.__sequence = (self.__sequence + 1) & sequence_mask
            if self.__sequence == 0:
                time.sleep(1 / self._mult)
                self.__sequence = 0
                return self._next_id()
        else:
            self.__sequence = 0
        self.__last_timestamp = current_time
        sequence = self.__sequence << machine_id_bits
        return ((current_time - self.start_epoch) << timestamp_left_shift) | self.worker_id | sequence

    def get_next_id(self):
        with self._lock:
            return self._next_id()

    def __next__(self):
        return self.get_next_id()

    def __iter__(self):
        return self
