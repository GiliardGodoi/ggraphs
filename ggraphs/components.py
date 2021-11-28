from .search import bfs

def connected_components(graph):
    '''
    It finds the connected components given a graph.

    Parameter
        graph : Graph

    Returns
        list of set:
            Return a list of connected components.
            Which components is represented by a set.

    Notes:
        This implementation is based in recursion and breadth search.
        By definition the sets must have empty intersection.
    '''
    all_nodes = set(graph.edges.keys())

    if not all_nodes:
        return {}

    def find_by_recursion(graph, start = None, nodes = None):
        if not start:
            return []
        if not nodes :
            return []

        visited = bfs(graph,start=start)

        not_visited = nodes - visited

        components = [visited]

        if len(not_visited):
            n_start = not_visited.pop()
            components += find_by_recursion(graph,start=n_start,nodes=not_visited)

        return components

    start = all_nodes.pop()

    return find_by_recursion(graph,start=start,nodes=all_nodes)
