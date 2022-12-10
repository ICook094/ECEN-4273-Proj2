# tests.py

import random
try:
    import unittest1 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):
    @unittest.skip("test name")
    def test_skipped(self):
        self.fail(###)

    def test_pass(self):
        self.assertEqual(###)

    def test_fail(self):
        self.assertEqual(###)
