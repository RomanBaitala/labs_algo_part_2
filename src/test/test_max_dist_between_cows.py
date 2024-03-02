import unittest
import sys

sys.path.append("D:\\University\\Algo_part_2\\labs_algo_part_2\\src\\")
from lab_2.max_dist_between_cows import max_dist_between_angry_cows


class TestMaxDistBetweenCows(unittest.TestCase):
    def test_sorted_free_section(self):
        result = max_dist_between_angry_cows([1, 8, 9, 11, 15, 20], 6, 4)
        self.assertEqual(result, 5)

    def test_free_sections_from_test_case(self):
        result = max_dist_between_angry_cows([1, 2, 8, 4, 9], 5, 3)
        self.assertEqual(result, 3)

    def test_all_elements_free_in_sector(self):
        result = max_dist_between_angry_cows(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            20,
            4,
        )
        self.assertEqual(result, 6)

    def test_elements_generated_by_chat_gpt(self):
        result = max_dist_between_angry_cows([1, 4, 8, 3, 15, 2], 6, 3)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
