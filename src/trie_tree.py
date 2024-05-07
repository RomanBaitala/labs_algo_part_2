"""_summary_
File gets string on input and returns trie tree
"""

class TrieNode:
    """_summary_
    class represent node of tire tree
    """
    def __init__(self, is_key: bool = False, data: str = '') -> None:
        self.is_key = is_key
        self.data = data
        self.children = {}


class TrieTree:
    """_summary_
    tire tree code implementation with methods: insert, find, delete
    """
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        """_summary_
        Inserting in TrieTree 

        Args:
            word (str): word we want to insert
        """
        current = self.root
        for i, letter in enumerate(word):
            if letter not in current.children:
                prefix = word[0:i+1]
                current.children[letter] = TrieNode(data=prefix)
            current = current.children[letter]
        current.is_key = True

    def find(self, word: str) -> object:
        """_summary_
        Function which finds certain word in tree
        Args:
            word (str): word we want to check 

        Returns:
            object: if we found the object else return None
        """
        current = self.root

        for letter in word:
            if letter not in current.children:
                return None
            current = current.children[letter]

        if current.is_key:
            return current
        return None

    def delete(self, word: str) -> str:
        """_summary_
        Realisation of deletind divides into two types. 
        First type, when we have large data we don't delete the letters from tree 
        but just set the certain is_key(equal to searched word) to False
        Second type, when we need to delete node with searched phrase and all parent nodes
        if they don't have children
        
        Args:
            word (str): searched word

        Returns:
            str: word which we deleted
        """

        searched_node = self.find(word)
        if searched_node.is_key:
            searched_node.is_key = False
        return searched_node.data

    def __find_child_words(self, current, words):
        if current.is_key:
            words.append(current.data)

        for letter in current.children:
            self.__find_child_words(current.children[letter], words)

    def prefix(self, pref: str) -> list:
        """_summary_
        Function finds all stored words with given prefix
        Args:
            pref (str): prefix of a word

        Returns:
            list: a list of a words starts with given prefix
        """
        current = self.root
        words = []
        for letter in pref:
            if letter not in current.children:
                return []
            current = current.children[letter]

        self.__find_child_words(current, words)
        return words


def trie_tree_fill(file_read: str) -> object:
    """_summary_
    Main function which gets the file to read. Read data from file and insert it to TrieTree

    Args:
        file_read (str): filename

    Returns:
        object: object of result tree
    """
    pattern_list = read_file(file_read)

    if len(pattern_list) == 0:
        return -1

    trie_tree = TrieTree()
    for line in pattern_list:
        for word in line:
            trie_tree.insert(word)

    return trie_tree


def read_file(filename: str) -> list:
    """_summary_

    Args:
        filename (str): _description_

    Returns:
        list: _description_
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            return [line.strip().split() for line in lines[0:]]
        return []
