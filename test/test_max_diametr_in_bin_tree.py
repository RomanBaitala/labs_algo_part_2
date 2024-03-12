import unittest
import sys

sys.path.append("D:\\University\\Algo_part_2\\labs_algo_part_2\\src\\")
from max_diametr_in_bin_tree import max_tree_diameter
from max_diametr_in_bin_tree import BinaryTree

root = BinaryTree(6)
root.left = BinaryTree(4)
root.right = BinaryTree(9)
root.right.right = BinaryTree(10)
root.right.right.right = BinaryTree(13)
root.left.right = BinaryTree(8)
root.left.right.right = BinaryTree(12)
root.left.right.right.right = BinaryTree(16)
root.left.left = BinaryTree(3)
root.left.left.left = BinaryTree(2)
root.left.left.left.left = BinaryTree(1)
root.left.left.left.left.left = BinaryTree(0)

class TestMaxDistBetweenCows(unittest.TestCase):
    def test_tree_diametr(self):
        result = max_tree_diameter(root)
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
