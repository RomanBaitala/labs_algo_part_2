"""This file has function gas_supply_between_city which finds cities
to which we can't transport gas
"""

from typing import List, Dict, Tuple


def dfs(graph: Dict[str, List[str]], start: str) -> list:
    """This function realise dfs with extra list visited
    Args:
        graph (Dict[str, List[str]]): graph of supply between cities
        start (str): start position in supply between cities

    Returns:
        list: cities which we can reach from gas storage
    """
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        for neighbour in graph[current]:
            stack.append(neighbour)
    return visited


def compare_gas_supplying(
    storage: str, visited: list, cities: list
) -> Tuple[str, List]:
    """This function compare two lists: visited & cities to find cities
    to which we can't transport gas

    Args:
        storage (str): gas storage name
        visited (list): list if visited city
        cities (list): list of all cities

    Returns:
        Tuple[str, List]: city name and list of cities to which we can't transport gas
    """
    differance = []
    for city in cities:
        if city not in visited:
            differance.append(city)
    return storage, differance


def gas_supply_between_cities(file_read: str, file_write: str):
    """This function create a graph from read data and uses functions
    dfs, compare_gas_supply to get the result and write it to file

    Args:
        file_read (str): name of file to read
        file_write (str): name of file to write
    """
    cities, storages, gas_lines = read_file(file_read)

    if len(cities) == 0:
        write_file(file_write, ['-1'])
        return

    unreachable = []

    graph = {city: [] for city in cities}
    for gas_line in gas_lines:
        source, destination = gas_line
        graph[source].append(destination)

    for storage in storages:
        visited = dfs(graph, storage)
        current_storage_info = compare_gas_supplying(storage, visited, cities)
        if len(current_storage_info[1]) == 0:
            continue
        unreachable.append(str(compare_gas_supplying(storage, visited, cities)))

    write_file(file_write, unreachable)


def read_file(filename: str) -> Tuple[List[str], List[str], List[List[str]]]:
    """This function gets filename to read. It parses that file and gets lists of
    cities, storages, pipelines

    Args:
        filename (str): name of filet oread

    Returns:
        Tuple[List[str], List[str], List[List[str]]]: tuple which include
        list of cities name, storages name and list of pipelines
    """
    cities = []
    storages = []
    gas_lines = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            cities = lines[0].strip().split()
            storages = lines[1].strip().split()
            gas_lines = [line.strip().split() for line in lines[2:]]

    cities = [city.replace(" ", "_") for city in cities]
    storages = [s.replace(" ", "_") for s in storages]
    return cities, storages, gas_lines


def write_file(filename, result):
    """This function writes the result to certain file

    Args:
        filename (_type_): name of file to write
        result (_type_): result to write into file
    """
    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as file:
        file.writelines(result)
