import graph
import heap

Vs=[1,2,3,4]
us=[1,1,2,2,3]
vs=[2,3,4,3,4]
ds=[1,2,4,6,99]
Vertices=[]

#v1=graph.Vertex(1,[graph.Edge(1,2,1,1),graph.Edge(1,3,2,2)])
#v2=graph.Vertex(2,[graph.Edge(2,4,4,4),graph.Edge(2,3,6,6)])
#v3=graph.Vertex(3,[graph.Edge(3,4,99,99)])
#v4=graph.Vertex(4,[])

#h=heap.Heap()
#
#h.insert(v4)
#h.insert(v3)
#h.insert(v2)
#h.insert(v1)
#h.insert(v3)
#h.insert(v4)
#h.insert(v1)
#h.insert(v2)
#h.insert(v4)
#h.insert(v3)
#h.insert(v2)
#h.insert(v1)
#h.insert(v3)
#h.insert(v1)
#h.insert(v2)
#h.insert(v4)
#h.insert(v4)
#h.insert(v1)
#h.insert(v2)
#
#h.printout()
#out=[]
#for i in range(len(h.nodes)):
#    out.append(h.extractmin().get_value())
#print out

########OK, heap works with arbitrary classes now. Dijkstra next

#1: Initialize with source vertex as root

#2: Add all other vertices with their value=float('inf')

#3: While heap not empty:
#   u=h.extractmin()
#   for all v, adj to u; check if v in minheap.
#   if v in minheap AND v.value > u.value+E(u,v).d:
#       v.value=u.value+E(u,v).d
def grow_a_graph(G,filename):
    G=graph.Graph
    
def do_a_dijkstra(G,root):
    root.value=0
    h=heap.Heap(root)
    for v in G.vertices:
        if v==root:
            continue
        v.value=float('inf')
        h.insert(v)
#test insertion in heap first
    print [i.value for i in h.nodes]
    print "inserted all points of G in h"
    print ""
    while len(h.nodes)>1:
        u=h.extractmin()

        print 'heap is ',[i.value for i in h.nodes] #OOPS, needs heapify!
        print [i.v_id for i in h.nodes]
        print "min vertex is ", u.v_id, "with ",len(u.edges), "edges"
        print 'edges of u are ',[[e.u.v_id,e.v.v_id,e.d] for e in u.edges]
        
        for E in u.edges:
            if (E.v in h.nodes) and E.v.value>u.value+E.d:
                E.v.value=u.value+E.d
                print "edge of u to", E.v.v_id,v.value, "with heap index ",h.nodes.index(E.v)
                h.check_parent(h.nodes.index(E.v)) 
                print [i.value for i in h.nodes] #OOPS, needs heapify!
                print [i.v_id for i in h.nodes]
        print ""

g1=graph.Graph()
v0=graph.Vertex(0)
v1=graph.Vertex(1)
v2=graph.Vertex(2)
v3=graph.Vertex(3)
v4=graph.Vertex(4)
v5=graph.Vertex(5)
v6=graph.Vertex(6)
v7=graph.Vertex(7)
v8=graph.Vertex(8)

v0.addedge(graph.Edge(v0,v1,4,4))
v0.addedge(graph.Edge(v0,v7,8,8))
v1.addedge(graph.Edge(v1,v2,8,8))
v1.addedge(graph.Edge(v1,v7,11,11))
v2.addedge(graph.Edge(v2,v3,7,7))
v2.addedge(graph.Edge(v2,v8,2,2))
v2.addedge(graph.Edge(v2,v5,4,4))
v3.addedge(graph.Edge(v3,v4,9,9))
v3.addedge(graph.Edge(v3,v5,14,14))
v4.addedge(graph.Edge(v4,v5,10,10))
v5.addedge(graph.Edge(v5,v6,2,2))
v6.addedge(graph.Edge(v6,v7,1,1))
v6.addedge(graph.Edge(v6,v8,6,6))
v7.addedge(graph.Edge(v7,v8,7,7))

g1.addvertices(v0)
g1.addvertices(v1)
g1.addvertices(v2)
g1.addvertices(v3)
g1.addvertices(v4)
g1.addvertices(v5)
g1.addvertices(v6)
g1.addvertices(v7)
g1.addvertices(v8)

do_a_dijkstra(g1,v0)
for v in g1.vertices:
    print v.value
