import random
import unittest
from collections import deque
from pathlib import Path

from ggraphs import UndirectedWeightedGraph as Graph
from ggraphs.steiner import (heuristic_prunning_kruskal,
                             heuristic_prunning_mst,
                             heuristic_shortest_path,
                             heuristic_shortest_path_origin,
                             heuristic_shortest_path_origin_prim)
from ggraphs.steiner.parser import ParserORLibrary

from .config import datasets_folder

@unittest.skipIf(
    not datasets_folder.exists(),
    "dataset folder doesn't exists"
)
class TestSTPGHeuristicas(unittest.TestCase):

    def setUp(self):

        self.stpg_instance = ParserORLibrary().parse(Path(datasets_folder, "steinb13.txt"))

        self.graph = self.stpg_instance.graph
        self.terminals = list(self.stpg_instance.terminals)

        random.seed()


    def test_instance_reading(self):

        stpg = self.stpg_instance

        self.assertEqual(stpg.nro_edges, 125)
        self.assertEqual(stpg.nro_nodes, 100)
        self.assertEqual(stpg.nro_terminals, 17)

        self.assertEqual(stpg.nro_terminals, len(stpg.terminals))
        self.assertEqual(stpg.nro_nodes, len(stpg.graph.vertices))

    def test_shortest_path(self):
        graph = self.graph
        stpg = self.stpg_instance

        terminal = random.choice(self.terminals)
        gg, cost = heuristic_shortest_path(graph, terminal, stpg.terminals)

        self.common_cases(gg, cost)

    def test_shortest_path_with_origin(self):

        graph = self.graph
        stpg = self.stpg_instance

        terminal = random.choice(self.terminals)
        gg, cost = heuristic_shortest_path_origin(graph, terminal, stpg.terminals)

        self.common_cases(gg, cost)

    def test_shortest_path_origin_prim(self):

        graph = self.graph
        stpg = self.stpg_instance

        terminal = random.choice(self.terminals)
        gg, cost = heuristic_shortest_path_origin_prim(graph, terminal, stpg.terminals)

        self.common_cases(gg, cost)

    def test_prunning_mst(self):

        graph = self.graph
        stpg = self.stpg_instance

        terminal = random.choice(self.terminals)
        gg, cost = heuristic_prunning_mst(graph, terminal, stpg.terminals)

        self.common_cases(gg, cost)


    def common_cases(self, steiner_tree : Graph, cost : int):

        self.assertIsInstance(steiner_tree, Graph)
        self.assertIsInstance(cost, int)
        self.assertGreater(cost,0)

        terminals = self.stpg_instance.terminals

        ## Se o v??rtice possui grau 1 ent??o ?? terminal. Mas se for terminal possui grau 1?
        degrees = { k : len(steiner_tree[k]) for k in steiner_tree.edges.keys() }
        for k, v in degrees.items() :
            if v == 1 :
                is_terminal = (k in terminals)
                self.assertTrue(is_terminal)

        all_vertices = set(steiner_tree.vertices)

        self.assertIsInstance(all_vertices, set)
        self.assertEqual(len(all_vertices), len(steiner_tree.vertices))

        ## todos os vertices terminais estao contidos na solu????o
        tt = terminals - all_vertices
        self.assertFalse(tt)

        ## Existe algum ponto de steiner na solu????o. Mas sempre isso vai acontecer?
        ss = all_vertices - terminals
        self.assertTrue(ss)

        stpg = self.stpg_instance
        has_cycles = self.check_cycles_dfs(steiner_tree, self.terminals[8])
        self.assertFalse(has_cycles)


    def check_cycles_dfs(self, graph, start):
        '''
            Verifica se existe um ciclo em um grafo a partir de um v??rtice.
            ?? claro, essa fun????o n??o foi testada.
        '''
        stack = deque()

        visited = set([start])
        prev = dict()

        stack.append(start)

        has_circle = False

        while stack:
            v = stack.pop()
            visited.add(v)
            for u in graph.adjacent_to(v):
                if u not in visited :
                    stack.append(u)
                    prev[u] = v
                elif not prev[v] == u :
                    has_circle = True

        return has_circle


if __name__ == "__main__" :
    unittest.main()
