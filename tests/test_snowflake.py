"""
Created by Purushot at 30/11/22
"""

__author__ = "Purushot14"

import ipaddress
import logging
from threading import Thread

from short_unique_id import get_next_snowflake_id
from short_unique_id.snowflake import (
    Snowflake,
    get_machine_id,
    get_process_id,
    get_worker_id,
    machine_id_bits,
    machine_id_mask,
    process_id_bits,
    process_id_mask,
    sequence_bits,
)
from tests import TestBase


class TestSnowflake(TestBase):
    def test_get_machine_id(self):
        machine_id_dict = {}
        for ip in ipaddress.ip_network("10.102.0.0/16"):
            machine_id = get_machine_id(str(ip))
            logging.info(f"IP : {ip}, machine_id {machine_id}")
            if _ip := machine_id_dict.get(machine_id):
                logging.info(
                    f"{'=*=' * 5} {_ip} {machine_id_dict.keys().__len__()}",
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

    def test_worker_id_bit_layout(self):
        """Verify process_id and machine_id occupy separate, non-overlapping bit fields."""
        worker_id = get_worker_id()
        machine_id = get_machine_id()
        process_id = get_process_id()

        # Extract fields from worker_id
        extracted_machine = worker_id & machine_id_mask
        extracted_process = (worker_id >> machine_id_bits) & process_id_mask

        self.assertEqual(extracted_machine, machine_id)
        self.assertEqual(extracted_process, process_id)

    def test_worker_id_different_processes(self):
        """Two different process_ids must produce different worker_ids for the same machine."""
        machine_id = get_machine_id()
        pid_a = 100
        pid_b = 200
        worker_a = ((pid_a & process_id_mask) << machine_id_bits) | machine_id
        worker_b = ((pid_b & process_id_mask) << machine_id_bits) | machine_id
        self.assertNotEqual(worker_a, worker_b)

    def test_snowflake_id_bit_fields_no_overlap(self):
        """Verify timestamp, sequence, process_id, and machine_id occupy distinct bit regions."""
        machine_id = 0b1010101010101010  # 16 bits
        process_id = 0b11001100  # 8 bits
        worker_id = (process_id << machine_id_bits) | machine_id

        snowflake = Snowflake(worker_id=worker_id)
        sid = snowflake.get_next_id()

        # Extract each field
        extracted_machine = sid & machine_id_mask
        extracted_process = (sid >> machine_id_bits) & process_id_mask
        extracted_sequence = (sid >> (machine_id_bits + process_id_bits)) & ((1 << sequence_bits) - 1)
        extracted_timestamp = sid >> (machine_id_bits + process_id_bits + sequence_bits)

        self.assertEqual(extracted_machine, machine_id)
        self.assertEqual(extracted_process, process_id)
        self.assertEqual(extracted_sequence, 0)  # first ID has sequence 0
        self.assertGreater(extracted_timestamp, 0)

    def test_sequence_increments_in_correct_field(self):
        """Rapid IDs must increment the sequence field without corrupting other fields."""
        machine_id = 0xABCD
        process_id = 0x12
        worker_id = (process_id << machine_id_bits) | machine_id

        snowflake = Snowflake(worker_id=worker_id, mult=10000)
        ids = [snowflake.get_next_id() for _ in range(5)]

        for sid in ids:
            extracted_machine = sid & machine_id_mask
            extracted_process = (sid >> machine_id_bits) & process_id_mask
            self.assertEqual(extracted_machine, machine_id)
            self.assertEqual(extracted_process, process_id)

        # All unique
        self.assertEqual(len(set(ids)), len(ids))

    def test_negative_cases(self):
        snowflake = Snowflake()
        self.assertRaises(ValueError, snowflake.set_mult, -1)
        self.assertRaises(ValueError, snowflake.set_mult, False)

        snowflake_id = snowflake.__iter__().__next__()
        self.assertIsInstance(snowflake_id, int)
