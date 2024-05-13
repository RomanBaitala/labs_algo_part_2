"""_summary_
"""

import unittest
import os
from src.wchain import find_max_chain

cur_path = os.path.dirname(__file__)


class TestWchain(unittest.TestCase):
    """
    Test class for word chain
    """

    def test_wchain_1(self):
        """_summary_
        Test case with normal data
        """
        find_max_chain(
            cur_path + "\\resources\\wchain.in",
            cur_path + "\\resources\\wchain.out"
        )
        with open(
            cur_path + "\\resources\\wchain.out", 'r', encoding='utf-8'
        ) as file:
            result = file.readline()

        self.assertEqual(int(result), 6)

    def test_wchain_2(self):
        """_summary_
        Test case with normal data
        """
        find_max_chain(
            cur_path + "\\resources\\wchain2.in",
            cur_path + "\\resources\\wchain2.out"
        )
        with open(
            cur_path + "\\resources\\wchain2.out", 'r', encoding='utf-8'
        ) as file:
            result = file.readline()

        self.assertEqual(int(result), 4)

    def test_wchain_3(self):
        """_summary_
        Test case with normal data
        """
        find_max_chain(
            cur_path + "\\resources\\wchain3.in",
            cur_path + "\\resources\\wchain3.out"
        )
        with open(
            cur_path + "\\resources\\wchain3.out", 'r', encoding='utf-8'
        ) as file:
            result = file.readline()

        self.assertEqual(int(result), 1)
