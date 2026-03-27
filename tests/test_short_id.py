"""
File: test_short_id
Author: prakash
Created: 20/05/25.
"""

__author__ = "prakash"
__date__ = "20/05/25"

from short_unique_id import generate_short_id
from short_unique_id.short_id import ORIGINAL, _int_to_base64
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

    def test_base64_uses_full_alphabet(self):
        """Encoding must use all 64 characters of the alphabet."""
        chars_used = set()
        # Encode values 0-63 to hit every remainder
        for i in range(64):
            chars_used.update(_int_to_base64(i))
        self.assertEqual(len(chars_used), 64)
        self.assertEqual(chars_used, set(ORIGINAL))

    def test_base64_unique_encoding(self):
        """Different integers must produce different strings."""
        encoded = [_int_to_base64(i) for i in range(10000)]
        self.assertEqual(len(set(encoded)), len(encoded))
