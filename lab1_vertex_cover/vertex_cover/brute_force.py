from itertools import combinations
from typing import Optional

from vertex_cover.types import VertexSets, EdgeList
from collections import deque


def check_solution(graph, in_cover):
    for v in range(1, len(graph)):
        for u in graph[v]:
            if not in_cover[u]:
                return False
    return True


def rekur(in_cover, graph, v, counter) -> bool:
    if v == len(graph):
        if counter > 0:
            return False
        return check_solution(graph, in_cover)
    if counter > 0:
        in_cover[v] = True
        with_vertex = rekur(in_cover, graph, v + 1, counter - 1)

        if with_vertex:
            return with_vertex
        in_cover[v] = False
    return rekur(in_cover, graph, v + 1, counter)

# TODO: add typing for graph

def brute_force(graph, k: int) -> Optional[set[int]]:
    """
    :param graph: graph represented as GRAPH REPRESENTATION?
    :param k: this many vertices have to cover the graphs
    :return: set of vertices that create the cover if the solution exists,
    otherwise None
    """
    n = len(graph)
    Q = deque()
    Q.append(1)
    In_cover = [False for i in range(n)]

    if rekur(In_cover, graph, 1, k):
        return set(filter(lambda x: x > 0, [i if In_cover[i] else 0 for i in range(n)]))

    return None
