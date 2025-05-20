"""
File: test_short_id
Author: prakash
Created: 20/05/25.
"""

__author__ = "prakash"
__date__ = "20/05/25"

from short_unique_id import generate_short_id
from tests import TestBase


class TestShortId(TestBase):
    def test_short_id(self):
        id1 = generate_short_id()
        id2 = generate_short_id()
        self.assertNotEqual(id1, id2)
        self.assertGreater(id2, id1)
        ids = [generate_short_id() for _ in range(1000)]
        for i in range(1, len(ids)):
            self.assertGreater(ids[i], ids[i - 1])

    def test_short_id_with_un_ordered(self):
        id1 = generate_short_id(is_ordered=False)
        id2 = generate_short_id(is_ordered=False)
        self.assertNotEqual(id1, id2)

    def test_short_id_with_mult(self):
        id1 = generate_short_id()
        id2 = generate_short_id(1000000)
        self.assertNotEqual(id1, id2)
        self.assertGreater(id2.__len__(), id1.__len__())
