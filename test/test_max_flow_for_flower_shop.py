"""_summary_
"""

import unittest
import os
from src.max_flow_for_flower_shop import max_flow

cur_path = os.path.dirname(__file__)


class TestMaxFlowForFlowerShop(unittest.TestCase):
    """
    Test class for function gas_supply_between_cities
    """

    def test_max_flow(self):
        """_summary_
        Test case with normal data
        """

        result = max_flow('resources/input_max_flow.csv')

        self.assertEqual(result, 20)

    def test_max_flow_multi_graph(self):
        """_summary_
        Test case with normal data
        """

        result = max_flow('resources/input_max_flow_multi_graph.csv')

        self.assertEqual(result, 0)

    def test_max_flow_with_1(self):
        """_summary_
        Test case with normal data
        """

        result = max_flow('resources/input_max_flow_with_1.csv')

        self.assertEqual(result, 4)

    def test_max_flow_empty(self):
        """_summary_
        Test case with normal data
        """

        result = max_flow('resources/input_max_flow_empty.csv')

        self.assertEqual(result, 0)
