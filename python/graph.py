class Vertex:
    def __init__(self,v_id=-1,edges=[],value=float('inf')):
        self.v_id=v_id
        self.edges=edges
        self.value=value #the distance value of the vertex from source v
    def addedge(self,E):
        self.edges.append(E)
    def get_shortest_edge():
        pass
    def get_value(self):
        if len(self.edges)>0: #temporary test, will return value otherwise
            return self.edges[0].get_value()
        else:
            return self.value


class Edge:
    def __init__(self,u, v, d=float('inf'),d1=float('inf')):
        self.u=u
        self.v=v
        self.d=d
        self.d1=d1
    def get_value(self):
        return self.d


class Graph:
    def __init__(self,Vertx=None):
        if Vertx!=None:
            if not Vertx.v_id in self.vertices:
                self.vertices.append(Vertx.v_id)
                self.addedges(Vertx.v_id)
        else:
            self.vertices=[]
            self.edges=[]

    def addedges(self,V):
        for edge in V.edges():
            self.edges.append([E.u,E.v,e.d,e.d1])

    def addvertices(self,V):
        if not V.v_id in self.vertices:
            self.vertices.append(V)
        self.addedges(V)

