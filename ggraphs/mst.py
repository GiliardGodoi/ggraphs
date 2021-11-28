from disjointset import DisjointSet
from pqueue import PriorityQueue
from .graph import UndirectedWeightedGraph as Graph

def prim(graph : Graph, start):
    ''' Prim's Algorithm: Compute the Minimum Spanning Tree for the graph.

    Parameters:
        graph : GraphDictionary
        start : <a graph's node>

    Returns:
        dict :

        int :

    TO DO:
        Verificar se para diferentes pontos de inicialização retorna a mesma árvore
        se sim, parece que está funcionando ok.
    '''
    if start not in graph.vertices:
        raise ValueError("start is not in graph vertices")

    mtree = dict()
    total_weight = 0
    pq = PriorityQueue()

    pq.push(0,(start, start))

    while pq :
        _, nodes = pq.pop()
        node_start, node_end = nodes
        if node_end not in mtree:
            mtree[node_end] = node_start
            total_weight += graph.weight(node_start, node_end)

            for next_node, weight in graph.edges[node_end].items():
                pq.push(weight,(node_end, next_node))

    return mtree, total_weight


def kruskal(graph : Graph):
    '''Kruskal Algorithm to determine a Minimum Spanning Tree froma a Graph

    Parameter
        graph : Graph

    Return
        Graph
    '''

    DS = DisjointSet()
    MST = Graph()

    for v in graph.vertices:
        DS.make_set(v)

    edges = [ {"edge" : (v, u), "weight" : graph.weight(v, u)}  \
                for v, u in graph.gen_undirect_edges()]

    edges = sorted(edges, key=lambda item: item["weight"])

    for item in edges:
        v, u = item["edge"]
        if DS.find(v) != DS.find(u):
            MST.add_edge(v, u, weight=item["weight"])
            DS.union(v,u)

    return MST