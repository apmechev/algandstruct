class Graph:
    def __init__(self,Vertx=None):
        from vertex import Vertex
        from edge import Edge
        if isinstance(Vertx,Vertex):
            if not Vertx.v_id in self.vertices:
                self.vertices.append(Vertx.v_id)
                self.add_edges(Vertx.v_id)
        else:
            self.vertices=[]
            self.edges=[]

    def add_edges(self,V):
        for E in V.edges:##Need to append not values u,v but instances where E.u=v.v_id
            self.edges.append([E.u,E.v,E.d,E.d1])

    def add_vertices(self,V):
        if not V.v_id in self.vertices:
            self.vertices.append(V)
        self.add_edges(V)
