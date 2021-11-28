from collections import defaultdict
from pqueue import PriorityQueue

def shortest_path_one_to_all(graph, source):
    ''' Dijkstra Algorithm: It computes the lowest distance between a source vertice and
    all the other vertices.

    Parameters
        graph : GraphDictionary
        source : <a vertice from the graph>

    Returns
        dist : dict
            <vertice : distance from source> - distance dictionary from the source to vertice
        prev : dict
            < vertice : previous > - a dictionary representing a previous node

    Notes:
        An early implementation has O(n^2) complexity.
        Many improvements has been proposed across the years.
        They are more complicated, though.

        Based in Chirantan Sharma's code
        <https://github.com/cs-oak/Fibonacci-Heaps/blob/master/dijkstra.py>
        Its use an other Priority Queue implemantation which is not used by Sharma.
    '''
    dist = defaultdict(lambda : float("inf"))
    dist[source] = 0

    prev = {source : None}
    done = {}

    pq = PriorityQueue()
    pq.push(0, (0, source))

    while not pq.empty():
        _, info = pq.pop()
        dist_u, u = info

        if u in done :
            continue

        done[u] = True

        for v in graph.edges[u]:
            new_dist_to_v = dist_u + graph.edges[u][v]
            # esse if só da False quando: o vertice ja estiver em dist (visitado) e a distancia ja for a menor
            if (not v in dist) or (dist[v] > new_dist_to_v):
                dist[v] = new_dist_to_v
                prev[v] = u
                pq.push(new_dist_to_v,(new_dist_to_v,v))

    return dist, prev