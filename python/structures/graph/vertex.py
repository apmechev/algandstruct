from structures.graph.edge import Edge


class Vertex:
    def __init__(self,v_id=-1):
        from structures.graph.edge import Edge
        self.v_id=v_id
        self.value=0
        self.edges=[]

    def add_edge(self,E): #Why does this add to all Vs?
        if isinstance(E,Edge):
             self.edges.append(E)
    def set_value(self,value):
        self.value=value
    def get_value(self):
         return self.value


