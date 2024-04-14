"""_summary_
"""

import unittest
import os
from src.gas_supply_between_storage_facilities import gas_supply_between_cities

cur_path = os.path.dirname(__file__)


class TestGasSupplyBetweenStorageFacilities(unittest.TestCase):
    """
    Test class for function gas_supply_between_cities
    """

    def test_gas_supply_between_cities(self):
        """_summary_
        Test case with normal data
        """
        gas_supply_between_cities(
            cur_path + "\\resources\\input_gas.txt",
            cur_path + "\\resources\\output_gas.txt"
        )

        with open(
            cur_path + "\\resources\\output_gas.txt",
            'r',
            encoding='utf-8'
        ) as file:
            first_line = file.readline().strip('( )').split(')(')

        self.assertEqual(len(first_line), 2)

    def test_gas_supply_empty(self):
        """_summary_
        Test case with empty file
        """
        gas_supply_between_cities(
            cur_path + "\\resources\\input_gas_supply_to_all.txt",
            cur_path + "\\resources\\output_gas_supply_to_all.txt"
        )

        with open(
                cur_path + "\\resources\\output_gas_supply_to_all.txt",
                'r',
                encoding='utf-8'
        ) as file:
            first_line = file.readline()

        self.assertEqual(first_line, '')

    def test_gas_supply_to_all_cities(self):
        """_summary_
        Test case when there are supply to all cities
        """
        gas_supply_between_cities(
            cur_path + "\\resources\\input_gas_empty.txt",
            cur_path + "\\resources\\output_gas_empty.txt"
        )

        with open(
                cur_path + "\\resources\\output_gas_empty.txt",
                'r',
                encoding='utf-8'
        ) as file:
            first_line = file.readline().strip('[ ]')

        self.assertEqual(int(first_line), -1)
