from collections import deque

def bfs(graph, start=None):
    '''Breadth First Search

    Parameters
        graph : GraphDictonary
        start : a graph's vertice

    Returns
        set
            a set of vertices reached

    Raises
        TypeError
        ValueError
    '''
    if not start:
        raise TypeError("Start is not defined")
    elif not (start in graph.vertices):
        raise ValueError("start node is not in graph")


    visited_nodes = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited_nodes.add(node)
        for v in graph.adjacent_to(node):
            if not v in visited_nodes:
                queue.append(v)

    return visited_nodes


def dfs(graph, start = None):
    '''Deep First Search

    Parameters
        graph : GraphDictionary
        start : graph's vertice

    Returns
        set
            vertices visited

    Raises:
        TypeError
        ValueError
    '''

    if not start :
        raise TypeError('Start is not defined')
    elif not (start in graph):
        raise ValueError("Start node is not in graph")

    vertices_done = set()
    stack = deque([start])

    while stack:
        node = stack.pop()
        vertices_done.add(node)
        for v in graph.adjacent_to(node):
            if not v in vertices_done:
                stack.append(v)

    return vertices_done