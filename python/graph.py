class Vertex:
    def __init__(self,v_id=-1):
        self.v_id=v_id
        self.edges=[]
    def addedge(self,E):#Why does this add to all Vs?
         self.edges.append(E)
    def get_value(self):
#        if len(self.edges)>0: #temporary test, will return value otherwise
#            return self.edges[0].get_value()
#        else:
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
        for E in V.edges:##Need to append not values u,v but instances where E.u=v.v_id
            self.edges.append([E.u,E.v,E.d,E.d1])

    def addvertices(self,V):
        if not V.v_id in self.vertices:
            self.vertices.append(V)
        self.addedges(V)
