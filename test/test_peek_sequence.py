import unittest
import sys

sys.path.append("D:\\University\\Algo_part_2\\labs_algo_part_2\\src\\")
from peek_sequence import peek_sequence


class TestPeekSequense(unittest.TestCase):
    def test_peek_sequence(self):
        result = peek_sequence([1, 3, 5, 4, 2, 8, 3, 7, 2])
        self.assertEqual(result, 5)

    def test_peek_sequence_lab_test(self):
        result = peek_sequence([3, 100, 2, 1, 7, 8, 9, 10, 9, 8, 7, 5, 120, 18])
        self.assertEqual(result, 9)

    def test_peek_seq_sorted_to_high(self):
        result = peek_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result, 0)

    def test_peek_seq_sorted_to_low(self):
        result = peek_sequence([9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(result, 0)

    def test_peek_seq_two_el(self):
        result = peek_sequence([1, 4])
        self.assertEqual(result, 0)

    def test_second_peek_seq(self):
        result = peek_sequence([1, 4, 5, 3, 4, 7, 9, 5, 3, 2, 8])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
