from ..graph import UndirectedWeightedGraph as Graph
from .parser import SteinerTreeProblem


def is_steiner_tree(subgraph : Graph, STPG: SteinerTreeProblem):
    '''Check if the graph passed is a Steiner Tree.

    Parameters:
        subgraph : Graph
            represent the partial solution to be tested
        STPG : SteinerTreeProblem
            the problem instance itself

    Returns:
        bool: True or False
        dict : status' test

    Note: A Steiner Tree might not be a Minimal Steiner Tree.
    '''
    is_steiner = True
    status = dict()

    terminals = STPG.terminals
    GRAPH = STPG.graph
    def is_terminal(v):
        return v in terminals

    # Rules to check
    status['has_cycle'] = has_cycle(subgraph)
    status['all_terminals_in'] = all(subgraph.has_node(t) for t in terminals)
    status['all_leaves_are_terminals'] = all(is_terminal(v) for v in subgraph.vertices if subgraph.degree(v) == 1)
    status['all_edges_are_reliable'] = all(GRAPH.has_edge(v,u) for v, u in subgraph.gen_undirect_edges())
    status['graph_is_connected'] = (how_many_components(subgraph) == 1)

    if status['has_cycle'] \
        or not status['all_terminals_in'] \
        or not status['all_leaves_are_terminals'] \
        or not status['all_edges_are_reliable'] \
        or not status['graph_is_connected'] :
        is_steiner = False

    return is_steiner, status

STEIN_B = [
    ("steinb1.txt",   82),  # 0
    ("steinb2.txt",   83),
    ("steinb3.txt",  138),
    ("steinb4.txt",   59),
    ("steinb5.txt",   61),  # 4
    ("steinb6.txt",  122),
    ("steinb7.txt",  111),
    ("steinb8.txt",  104),
    ("steinb9.txt",  220),  # 8
    ("steinb10.txt",  86),
    ("steinb11.txt",  88),
    ("steinb12.txt", 174),
    ("steinb13.txt", 165),  # 12
    ("steinb14.txt", 235),
    ("steinb15.txt", 318),  # 14
    ("steinb16.txt", 127),  # 15
    ("steinb17.txt", 131),  # 16
    ("steinb18.txt", 218),  # 17
]

STEIN_C = [
    ("steinc1.txt", 85),
    ("steinc2.txt", 144),
    ("steinc3.txt", 754),
    ("steinc4.txt", 1079),
    ("steinc5.txt", 1579),
    ("steinc6.txt", 55),
    ("steinc7.txt", 102),
    ("steinc8.txt", 509),
    ("steinc9.txt", 707),
    ("steinc10.txt", 1093),
    ("steinc11.txt", 32),
    ("steinc12.txt", 46),
    ("steinc13.txt", 258),
    ("steinc14.txt", 323),
    ("steinc15.txt", 556),
    ("steinc16.txt", 11),
    ("steinc17.txt", 18),
    ("steinc18.txt", 113),
    ("steinc19.txt", 146),
    ("steinc20.txt", 267),
]

STEIN_D = [
    ("steind1.txt", 106),
    ("steind2.txt", 220),
    ("steind3.txt", 1565),
    ("steind4.txt", 1935),
    ("steind5.txt", 3250),
    ("steind6.txt", 67),
    ("steind7.txt", 103),
    ("steind8.txt", 1072),
    ("steind9.txt", 1448),
    ("steind10.txt", 2110),
    ("steind11.txt", 29),
    ("steind12.txt", 42),
    ("steind13.txt", 500),
    ("steind14.txt", 667),
    ("steind15.txt", 1116),
    ("steind16.txt", 13),
    ("steind17.txt", 23),
    ("steind18.txt", 223),
    ("steind19.txt", 310),
    ("steind20.txt", 537),
]


STEIN_E = [
    ("steine1.txt", 111),
    ("steine2.txt", 214),
    ("steine3.txt", 4013),
    ("steine4.txt", 5101),
    ("steine5.txt", 8128),
    ("steine6.txt", 73),
    ("steine7.txt", 145),
    ("steine8.txt", 2640),
    ("steine9.txt", 3604),
    ("steine10.txt", 5600),
    ("steine11.txt", 34),
    ("steine12.txt", 67),
    ("steine13.txt", 1280),
    ("steine14.txt", 1732),
    ("steine15.txt", 2784),
    ("steine16.txt", 15),
    ("steine17.txt", 25),
    ("steine18.txt", 564),
    ("steine19.txt", 758),
    ("steine20.txt", 1342),
]

# If the number in the Opt column is written in italics
# the optimum is not known.
# The number given is the best know upper bound.
# See more at <http://steinlib.zib.de/showset.php?PUC>

PUC = [
    ("bip42p", 24657),
    ("bip42u", 236),
    ("bip52p", 24526),
    ("bip52u", 234),
    ("bip62p", 22843),
    ("bip62u", 219),
    ("bipa2p", 35326),
    ("bipa2u", 338),
    ("bipe2p", 5616),
    ("bipe2u", 54),
    ("cc10-2p", 35297),
    ("cc10-2u", 342),
    ("cc11-2p", 63491),
    ("cc11-2u", 612),
    ("cc12-2p", 121106),
    ("cc12-2u", 1172),
    ("cc3-10p", 12772),
    ("cc3-10u", 125),
    ("cc3-11p", 15582),
    ("cc3-11u", 153),
    ("cc3-12p", 18826),
    ("cc3-12u", 185),
    ("cc3-4p", 2338),
    ("cc3-4u", 23),
    ("cc3-5p", 3661),
    ("cc3-5u", 36),
    ("cc5-3p", 7299),
    ("cc5-3u", 71),
    ("cc6-2p", 3271),
    ("cc6-2u", 32),
    ("cc6-3p", 20270),
    ("cc6-3u", 197),
    ("cc7-3p", 56799),
    ("cc7-3u", 549),
    ("cc9-2p", 17199),
    ("cc9-2u", 167),
    ("hc10p", 59797),
    ("hc10u", 575),
    ("hc11p", 119492),
    ("hc11u", 1145),
    ("hc12p", 236949),
    ("hc12u", 2262),
    ("hc6p", 4003),
    ("hc6u", 39),
    ("hc7p", 7905),
    ("hc7u", 77),
    ("hc8p", 15322),
    ("hc8u", 148),
    ("hc9p", 30242),
    ("hc9u", 292)
]
