# -*- coding: utf-8 -*-

from .context import testbot

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        testbot.hmm()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()