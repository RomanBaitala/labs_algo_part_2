import unittest
from src.red_black_priority_queue import RedBlackTree


class TestRedBlackPriorityQueue(unittest.TestCase):
    def test_peek_sequence(self):
        tree = RedBlackTree()
        tree.insert('131', 5)
        tree.insert('fsd', 6)
        tree.insert('rwt', 7)
        tree.insert('tyu', 3)
        tree.insert('rtu', 9)
        tree.insert('rtu', 8)
        tree.insert('rtu', 4)
        self.assertEqual(tree.delete(), 'rtu')


if __name__ == "__main__":
    unittest.main()
