class Edge(object):
    def __init__(self,u, v, d=float('inf')):
        from structures.graph.vertex import Vertex
        if isinstance(u,Vertex) and isinstance(v,Vertex):
            self.u=u
            self.v=v
        else:
            raise AttributeError("u or v not a vertex")
        self.d=d

    @property
    def u(self):
        return self._u

    @property
    def d(self):
        return self._d

    @property
    def v(self):
        return self._v

    @u.setter
    def u(self,value):
        self._u=value
    
    @v.setter
    def v(self,value):
        self._v=value

    @d.setter
    def d(self,value):
        self._d=value


class PositiveEdge(Edge):
    def __init__(self,u, v, d=float('inf')):
        if d<0:
            raise ValueError("Negative Edges Forbidden")
        super(PositiveEdge, self).__init__(u,v,d)

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self,value):
        if d<0:
            raise ValueError("Negative Edges Forbidden")
        self._d=value

