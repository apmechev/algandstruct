import unittest

from structures.graph.edge import Edge
from structures.graph.edge import Edge
from structures.graph.edge import PositiveEdge
from structures.graph.vertex import Vertex


class testEdge(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_neg_pos_edge(self):
        V=Vertex()
        W=Vertex()
        e=Edge(V,W,-10)
        self.assertTrue(e.d==-10)
        f=Edge(V,W,10)
        self.assertTrue(f.d==10)
        g=Edge(V,W,0)
        self.assertTrue(g.d==0)

    def test_neg_only_edge(self):
        V=Vertex()
        W=Vertex()
        e=PositiveEdge(V,W,10)
        self.assertTrue(e.d==10)
        self.assertRaises(ValueError,PositiveEdge,V,W,-10)
        g=PositiveEdge(V,W,0)
        self.assertTrue(g.d==0)


