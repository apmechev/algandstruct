from structures.graph.vertex import Vertex
V=Vertex(0)
help(V)

from structures.graph.edge import Edge
help(Edge)
U=Vertex(1)
W=Vertex(2)
e=Edge(U,V)
U.add_edge(e)

