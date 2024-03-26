"""_summary_
The function takes matrix with '1' and '0'. Elements '1' it's ground and '0' ones it's water.
Function calculates the number of islands and returns this number
"""
from typing import List

def bfs(graph: List[List[int]], x: int, y: int, visited: set):
    """_summary_
    This function do the bfs when find element with value '1' when it isn't already 
    visited
    Args:
        graph (List[List[int]]): _description_
        x (int): x coordinate
        y (int): y coordinate
        visited (set): elements with value 1 which was already visited
    """

    queue = [(y, x)]

    while queue:
        y, x = queue.pop(0)
        visited.add((y, x))
        neighbours = find_neighbours(graph, x, y)
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)


def find_neighbours(graph: List[List[int]], x: int, y: int) -> list:
    """_summary_
    This function finds all elements which is connected to the currnet element
    Args:
        graph (List[List[int]]): two dementional matrix
        x (int): x coordinate
        y (int): y coordinate

    Returns:
        list: returns all neighbours of current element
    """
    neighbour = []
    cords = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for cols, rows in cords:
        if len(graph) - 1 >= abs(y + cols) and len(graph) - 1 >= abs(x + rows):
            if graph[abs(y + cols)][abs(x + rows)]:
                neighbour.append((abs(y + cols), abs(x + rows)))
    return neighbour


def read_input(file_name) -> List[List[int]]:
    """_summary_
    This function parse data to matrix from given file and returns it 
    Args:
        file_name (file): file to read data from 

    Returns:
        List[List[int]]: this function retuns matrix read from file
    """
    input_matrix = []
    with open(
        file_name,
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            row = list(map(int, line.split(",")))
            input_matrix.append(row)
    file.close()
    return input_matrix


def write_output(filename, result):
    """_summary_

    Args:
        filename (_type_): _description_
        result (_type_): _description_
    """
    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(str(result))


def find_islands(filename_read, filename_write):
    """_summary_
    This function finds number of islands in matrix
    Args:
        filename_read (str): file to read data from 
        filename_write (str): file to write result in 
    """
    graph = read_input(filename_read)

    if len(graph) == 0 or len(graph[0]) == 0:
        write_output(filename_write, -1)
        return

    rows = len(graph)
    cols = len(graph[0])
    visited = set()
    island_count = 0

    for y in range(rows):
        for x in range(cols):
            if graph[y][x] == 1:
                if (y, x) not in visited:
                    island_count += 1
                bfs(graph, x, y, visited)
    write_output(filename_write, island_count)
