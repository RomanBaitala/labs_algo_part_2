"""_summary_
Implementation of Ford-Fulkerson algorithm using dfs.
Function max_flow() finds the maximum flow to given graph
Returns:
    _type_: max flow 
"""
from typing import Tuple, List, Dict


def dfs(
    graph: Dict[str, Dict[str, int]], start: str, destination: str
) -> Tuple[List[Tuple[str, str]], int]:
    """_summary_
    Implementing of the dfs which uses adjacency list to iterate. Function returns path 
    from start point to end point and minimal edge weight in that path. 
    Args:
        graph (Dict[str, Dict[str, int]]): graph given in adjacency list format 
        start (str): start point
        destination (str): end point

    Returns:
        Tuple[List[Tuple[str, str]], int]: path from start point to end point 
        and minimal edge weight
    """
    stack = [(start, float("inf"), None)]
    visited = set()
    path = []
    min_weight = float("inf")
    while stack:
        current_element, weight, parent = stack.pop()

        if parent:
            for p in path.copy():
                if p[0] == parent:
                    path.remove(p)
            path.append((parent, current_element))
        min_weight = min(min_weight, weight)
        if current_element == destination or current_element not in graph:
            break

        visited.add(current_element)
        for vertex, edge_weight in graph[current_element].items():
            if vertex in visited:
                continue
            stack.append((vertex, edge_weight, current_element))
    if (not stack and len(path) == 0
            or path[0][0] != start or path[-1][1] != destination):
        return [], 0

    return path, min_weight


def decrease_weight(
    graph: Dict[str, Dict[str, int]], path: List[Tuple[str, str]], current_flow: int
):
    """_summary_
    Function decreases edges weight on the given path and deletes edges with
    weight equals 0
    Args:
        graph (Dict[str, Dict[str, int]]): graph given in adjacency list format 
        path (List[Tuple[str, str]]): path from start point to end point
        current_flow (int): max flow in current path 
    """
    for edge in path:
        graph[edge[0]][edge[1]] -= current_flow
        if graph[edge[0]][edge[1]] == 0:
            del graph[edge[0]][edge[1]]


def max_flow(filename: str) -> int:
    """_summary_
    Function uses previously implemented functions to find
    maximum flow
    Args:
        filename (str): name of the file to read from

    Returns:
        int: max flow in given graph
    """
    begin, destination, graph = read_file(filename)
    max_flow_value = 0
    while True:
        path, found_flow = dfs(graph, begin, destination)

        if found_flow == 0 or path[0][0] != 'GF':
            break

        max_flow_value += found_flow
        decrease_weight(graph, path, found_flow)

    return max_flow_value


def read_file(file_path: str) -> Tuple[str, str, Dict]:
    """_summary_
    Function read data from file in format 
    F1,F2,F3 -> start points
    S1,S2,S3 -> end points
    F1,R1,5 -> edges where (F1 and R1 vertexes and 5 is weight)
    Function returns start and end points which is similar for all situations.
    It's made to make better performance when we have more than one start and end 
    points. Adjacency list it's a format in which I create my graph from given data.
    Args:
        file_path (str): path to file 

    Returns:
        Tuple[str, str, Dict]: start point, end point, adjacency list
    """
    adjacency_list = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        farms = file.readline().strip().split(',')
        shops = file.readline().strip().split(',')
        adjacency_list["GF"] = {farm: float('inf') for farm in farms}
        for shop in shops:
            if shop not in adjacency_list:
                adjacency_list[shop] = {"GS": float('inf')}

        for line in file:
            source, destination, weight = line.strip().split(',')
            if source not in adjacency_list:
                adjacency_list[source] = {}
            adjacency_list[source][destination] = int(weight)
    return "GF", "GS", adjacency_list
