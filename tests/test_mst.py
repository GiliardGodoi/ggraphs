import unittest
from os import path

from ggraphs import UndirectedWeightedGraph as Graph
from ggraphs.mst import prim
from ggraphs.steiner.parser import ParserORLibrary

class TestMinimumSpanningTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        arquivo = path.join("datasets", "ORLibrary", "steinb1.txt")

        cls.stp = ParserORLibrary().parse(arquivo)
        cls.graph = cls.stp.graph

    def test_mst_cost(self):
        start_node = 34
        _, cost = prim(self.graph, start_node)

        self.assertGreater(cost,0)
        self.assertEqual(cost,238)


if __name__ == "__main__" :
    unittest.main()