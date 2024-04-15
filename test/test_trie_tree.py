"""_summary_
"""

import unittest
import os
from src.trie_tree import trie_tree_fill

cur_path = os.path.dirname(__file__)


class TestTrieTree(unittest.TestCase):
    """
    Test class for function trie_tree_fill
    """

    def test_trie_tree_fill(self):
        """_summary_
        Test case with normal data
        """
        result = trie_tree_fill(
            cur_path + "\\resources\\input_trie.txt",
        )

        self.assertEqual(len(result.prefix('fer')), 3)

    def test_trie_tree_empty(self):
        """_summary_
        Test case with empty file
        """
        result = trie_tree_fill(
            cur_path + "\\resources\\input_trie_empty.txt"
        )

        self.assertEqual(result, -1)
