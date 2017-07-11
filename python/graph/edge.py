class Edge:
    def __init__(self,u, v, d=float('inf'),d1=float('inf')):
        from vertex import Vertex
        if isinstance(u,Vertex) and isinstance(v,Vertex):
            self.u=u
            self.v=v
        else:
            raise("u or v not a vertex")
        self.d=d
        self.d1=d1
    def get_value(self):
        return self.d



