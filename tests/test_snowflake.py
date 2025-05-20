"""Created by Purushot at 30/11/22
"""

__author__ = "Purushot14"

import ipaddress
import logging
from threading import Thread

from short_unique_id import get_next_snowflake_id
from short_unique_id.snowflake import Snowflake, get_machine_id
from tests import TestBase


class TestSnowflake(TestBase):
    def test_get_machine_id(self):
        machine_id_dict = {}
        for ip in ipaddress.ip_network("10.102.0.0/16"):
            machine_id = get_machine_id(str(ip))
            logging.info(f"IP : {ip}, machine_id {machine_id}")
            if _ip := machine_id_dict.get(machine_id):
                logging.info(
                    f'{"=*=" * 5} {_ip} {machine_id_dict.keys().__len__()}',
                )
            else:
                logging.info(f"==== {machine_id_dict.keys().__len__()}")
                machine_id_dict[machine_id] = ip

    def test_get_next_id(self):
        snowflake = Snowflake()
        get_next_snowflake_id = snowflake.get_next_id()
        logging.info(f"get_next_snowflake_id : {get_next_snowflake_id}")
        snowflake_id2 = snowflake.get_next_id()
        logging.info(f"get_next_snowflake_id : {snowflake_id2}")
        self.assertGreater(snowflake_id2, get_next_snowflake_id)
        snowflake_ids = [snowflake.__next__() for i in range(1, 10000)]
        self.assertEqual(set(snowflake_ids).__len__(), snowflake_ids.__len__())
        for i, val in enumerate(snowflake_ids[1:]):
            self.assertGreater(val, snowflake_ids[i])

    def test_concurrent_get_next_id(self):
        snowflake = Snowflake(mult=1000)
        snowflake_ids = []
        threads = []
        for i in range(1, 10000):  # noqa B007
            thread = Thread(target=lambda: snowflake_ids.append(snowflake.__next__()))
            thread.start()
            threads.append(thread)
        [thread.join() for thread in threads]
        logging.info(f"threads length {threads.__len__()} snowflake ids length {snowflake_ids.__len__()}")
        self.assertEqual(set(snowflake_ids).__len__(), snowflake_ids.__len__())
        for i, val in enumerate(snowflake_ids[1:]):
            self.assertGreater(val, snowflake_ids[i])

    def test_snowflake_id(self):
        _snowflake_id = get_next_snowflake_id()
        logging.info(f"get_next_snowflake_id : {_snowflake_id}")
        snowflake_id2 = get_next_snowflake_id()
        logging.info(f"get_next_snowflake_id : {snowflake_id2}")
        self.assertGreater(snowflake_id2, _snowflake_id)
        snowflake_ids = [get_next_snowflake_id() for i in range(1, 10000)]
        self.assertEqual(set(snowflake_ids).__len__(), snowflake_ids.__len__())
        for i, val in enumerate(snowflake_ids[1:]):
            self.assertGreater(val, snowflake_ids[i])

    def test_concurrent_snowflake_id(self):
        snowflake_ids = []
        threads = []
        for i in range(1, 10000):  # noqa B007
            thread = Thread(target=lambda: snowflake_ids.append(get_next_snowflake_id()))
            thread.start()
            threads.append(thread)
        [thread.join() for thread in threads]
        logging.info(f"threads length {threads.__len__()} snowflake ids length {snowflake_ids.__len__()}")
        self.assertEqual(set(snowflake_ids).__len__(), snowflake_ids.__len__())
        for i, val in enumerate(snowflake_ids[1:]):
            self.assertGreater(val, snowflake_ids[i])
