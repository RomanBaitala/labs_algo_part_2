"""_summary_
Finds the longest chain of words
"""
from typing import List


def find_max_chain(readfile: str, writefile: str):
    """_summary_
    Main function using sotring from low len to high. Using for loops to find words and 
    calculate chain lenth
    Args:
        readfile (str): file name to read 
        writefile (str): file name to write
    """
    word_list = read_file(readfile)
    word_list.sort(key=len)
    word_table = {word: 1 for word in word_list}
    for word in word_list:
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in word_table:
                word_table[word] = max(word_table[word], word_table[new_word]+1)

    write_file(writefile, max(word_table.values()))


def read_file(filename: str) -> List[str]:
    """_summary_

    Args:
        filename (str): file to read

    Returns:
        List[str]: given list of word
    """
    with open(filename, 'r', encoding='utf-8') as file:
        number_of_words = int(file.readline().strip())
        word_list = [file.readline().strip() for _ in range(number_of_words)]
    return word_list


def write_file(filename: str, result: int):
    """_summary_

    Args:
        filename (str): file name to wtite
        result (int): result get in main function
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(result))
