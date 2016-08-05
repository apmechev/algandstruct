import graph
import heap

Vs=[1,2,3,4]
us=[1,1,2,2,3]
vs=[2,3,4,3,4]
ds=[1,2,4,6,99]
Vertices=[]

v1=graph.Vertex(1,[graph.Edge(1,2,1,1),graph.Edge(1,3,2,2)])
v2=graph.Vertex(2,[graph.Edge(2,4,4,4),graph.Edge(2,3,6,6)])
v3=graph.Vertex(3,[graph.Edge(3,4,99,99)])
v4=graph.Vertex(4,[])

h=heap.Heap()

h.insert(v4)
h.insert(v3)
h.insert(v2)
h.insert(v1)
h.insert(v3)
h.insert(v4)
h.insert(v1)
h.insert(v2)
h.insert(v4)
h.insert(v3)
h.insert(v2)
h.insert(v1)
h.insert(v3)
h.insert(v1)
h.insert(v2)
h.insert(v4)
h.insert(v4)
h.insert(v1)
h.insert(v2)

h.printout()
out=[]
for i in range(len(h.nodes)):
    out.append(h.extractmin().edges)
print out

