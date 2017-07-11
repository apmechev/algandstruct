from graph import graph
from heap import heap

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
    G=graph.Graph()
    with open(filename,'r') as gfile:
        lines = gfile.readlines()
    verts=lines[0].strip().split()[0]
    contents=[]
    for i in range(len(lines)):
        contents.append([int(n) for n in lines[i].strip().split()])
    print contents[0:10]

    vert_objs=[]
    vert_objs.append(graph.Vertex(0))#v0 used in BF
    print verts
    for i in range(1,int(verts)+1):
        vert_objs.append(vertex.Vertex(i))

    j=1#current vertex (assumes the input file is sorted by tail vertex)
    for i in range(1,len(contents)):
        if contents[i][0]==vert_objs[j].v_id:
            vert_objs[j].addedge(edge.Edge(vert_objs[j],vert_objs[contents[i][1]],int(contents[i][2]),int(contents[i][2])))
            
        else:
            j+=1
            vert_objs[j].addedge(edge.Edge(vert_objs[j],vert_objs[contents[i][1]],int(contents[i][2]),int(contents[i][2])))
    return vert_objs

def do_a_dijkstra(G,root):
    root.value=0
    h=heap.Heap(root)
    for v in G.vertices:
        if v==root:
            continue
        v.value=float('inf')
        h.insert(v)
    while len(h.nodes)>1:
        m=h.extractmin()
        ##Only works for directed graphs, otherwise would have to match 
        for E in m.edges:
            if (E.v in h.nodes) and E.v.value>m.value+E.d:
                E.v.value=m.value+E.d
                h.check_parent(h.nodes.index(E.v)) 
        print ".",

g1=graph.Graph()
g2=graph.Graph()
vs=grow_a_graph(g1,"/home/apmechev/MOOCS/Algo2/s4/g1.txt")
#vs=grow_a_graph(g1,"test.txt")
g1.addvertices(vertex.Vertex(0))
for i in range(1,len(vs)):
    g1.addvertices(vs[i])


v0=vertex.Vertex(0)
v1=vertex.Vertex(1)
v2=vertex.Vertex(2)
v3=vertex.Vertex(3)
v4=vertex.Vertex(4)
v5=vertex.Vertex(5)
v6=vertex.Vertex(6)
v7=vertex.Vertex(7)
v8=vertex.Vertex(8)
v9=vertex.Vertex(9)
v10=vertex.Vertex(10)
#
##UNDIRECTED Test case (won't efficiently work with heap (NOT IMPLEMENTED CORRECTLY ))
v0.addedge(edge.Edge(v0,v1,4,4))
v0.addedge(edge.Edge(v0,v7,8,8))
v1.addedge(edge.Edge(v1,v2,8,8))
v1.addedge(edge.Edge(v1,v7,11,11))
v2.addedge(edge.Edge(v2,v3,7,7))
v2.addedge(edge.Edge(v2,v8,2,2))
v2.addedge(edge.Edge(v2,v5,4,4))
v3.addedge(edge.Edge(v3,v4,9,9))
v3.addedge(edge.Edge(v3,v5,14,14))
v4.addedge(edge.Edge(v4,v5,10,10))
v5.addedge(edge.Edge(v5,v6,2,2))
v6.addedge(edge.Edge(v6,v7,1,1))
v6.addedge(edge.Edge(v6,v8,6,6))
v7.addedge(edge.Edge(v7,v8,7,7))
#
##Directed test case
#v0.addedge(graph.Edge(v0,v1,3,3))
#v0.addedge(graph.Edge(v0,v2,4,4))
#v1.addedge(graph.Edge(v1,v2,6,6))
#v1.addedge(graph.Edge(v1,v4,7,7))
#v1.addedge(graph.Edge(v1,v3,2,2))
#v2.addedge(graph.Edge(v2,v4,5,5))
#v3.addedge(graph.Edge(v3,v4,1,1))
#v3.addedge(graph.Edge(v3,v5,8,8))
#v4.addedge(graph.Edge(v4,v5,4,4))
#
##Another directed case
##v1.addedge(graph.Edge(v1,v2,2,2))
##v1.addedge(graph.Edge(v1,v3,20,20))
##v2.addedge(graph.Edge(v2,v4,3,3))
##v4.addedge(graph.Edge(v4,v5,0,0))
##v5.addedge(graph.Edge(v5,v6,6,6))
##v6.addedge(graph.Edge(v6,v3,2,2))
##v5.addedge(graph.Edge(v5,v7,4,4))
##v5.addedge(graph.Edge(v5,v8,1,1))
##v7.addedge(graph.Edge(v7,v6,1,1))
##v7.addedge(graph.Edge(v7,v5,2,2))
##v8.addedge(graph.Edge(v8,v9,7,7))
##v9.addedge(graph.Edge(v9,v10,5,5))
##v10.addedge(graph.Edge(v10,v8,0,0))
#
##another directed test case
g2.addvertices(v0)
g2.addvertices(v1)
g2.addvertices(v2)
g2.addvertices(v3)
g2.addvertices(v4)
g2.addvertices(v5)
g2.addvertices(v6)
g2.addvertices(v7)
g2.addvertices(v8)
##g1.addvertices(v9)
##g1.addvertices(v10)

import numpy as np
def Bellman_Ford(g,v0):
    n_ver=len(g.vertices)
    A=np.zeros(n_ver)
    A.fill(float('inf'))
    A[v0.v_id]=0
    B=np.zeros(n_ver) 
    B.fill(float('inf'))
    B[v0.v_id]=0
    #Initialized all distances to inf, except distance of vs to itself
    for i in range(len(g.vertices)-1):#change to numvert
        for v in range(len(g.vertices)):
            prev=A[v]
            for e in g.edges:
                if v !=e[1].v_id:
                    continue
                if prev > A[e[0].v_id]+e[2]:
                    B[v]=A[e[0].v_id]+e[2]
                else:
                    B[v]=A[v]
                A=list(B) 
    return A




def re_weigh(g,p_v):
    gp=graph.Graph()
    for e in g.edges:
        e[2]=e[3]+p_v[e[0].v_id]-p_v[e[1].v_id]
    return g

def de_weigh(g,p_v):
    for e in g.edges:
        e[3]=e[2]-p_v[e[0].v_id]+p_v[e[1].v_id]
        e[2]=e[3]
    return g
#for v in g1.vertices:
#    print v.value, BF[v.v_id-1],v.v_id

def Johnson(infile):
    g=graph.Graph()
    vs=grow_a_graph(g,infile)
    v0=vertex.Vertex(0)
    ix=0
    for i in range(len(vs)):
        print ix
        ix+=1
        v0.addedge(edge.Edge(v0,vs[i],0,0))
    for e in v0.edges:
        print "v0 has edge to", e.v.v_id," with len ",e.d
    vs=[v0]+vs[1:]

    for i in range(len(vs)): 
        g.addvertices(vs[i])
    p_v=Bellman_Ford(g,vs[0])

    print p_v
    g.edges=g.edges[len(g.vertices[0].edges):]
    g.vertices=g.vertices[1:] #remove artificial zero vertex
    gw=re_weigh(g,p_v)
    for e in gw.edges:
        print e[0].v_id,"->",e[1].v_id,"was",e[3],"now is",e[2]
    results=[]
    for v in gw.vertices:
        gp=gw
        do_a_dijkstra(gp,v)
        gp=de_weigh(gp,p_v)
        results.append([v.value for v in gp.vertices])
    print results
    print min([min(x) for x in results])

Johnson("/home/apmechev/MOOCS/Algo2/s4/g3.txt")
Johnson("test.txt")
