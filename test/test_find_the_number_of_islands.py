"""_summary_
"""
import unittest
import os
from src.find_the_number_of_islands import find_islands

cur_path = os.path.dirname(__file__)


class TestFindTheNuberOfIslands(unittest.TestCase):
    """_summary_
    Test class for testing finding the island number
    """

    def test_find_number_in_null_matrix(self):
        """_summary_
        Test function which gives None on the input
        """
        find_islands(
            cur_path + "\\resources\\input_island_empty.txt",
            cur_path + "\\resources\\output_island_empty.txt",
        )
        with open(
            cur_path + "\\resources\\output_island_empty.txt",
            "r",
            encoding="utf-8",
        ) as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), -1)

    def test_find_number_of_islands_in_matrix_10x10(self):
        """_summary_
        Test function which gives matrix 10x10 size on the input
        """
        find_islands(
            cur_path + "\\resources\\input_island.txt",
            cur_path + "\\resources\\output_island.txt",
        )
        with open(
            cur_path + "\\resources\\output_island.txt",
            "r",
            encoding="utf-8",
        ) as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), 5)

    def test_find_number_of_island_in_matrix_1(self):
        """_summary_
        Test function which gives matrix with only "1" elements on the input
        """
        find_islands(
            cur_path + "\\resources\\input_island_with_1.txt",
            cur_path + "\\resources\\output_island_with_1.txt",
        )
        with open(
            cur_path + "\\resources\\output_island_with_1.txt",
            "r",
            encoding="utf-8",
        ) as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), 1)

    def test_find_number_of_island_in_matrix_0(self):
        """_summary_
        Test function which gives matrix with only "1" elements on the input
        """
        find_islands(
            cur_path + "\\resources\\input_island_with_0.txt",
            cur_path + "\\resources\\output_island_with_0.txt",
        )
        with open(
            cur_path + "\\resources\\output_island_with_0.txt",
            "r",
            encoding="utf-8",
        ) as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), 0)


if __name__ == "__main__":
    unittest.main()
