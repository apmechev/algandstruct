##Slightly less simple Heap Data-structure 

class Heap:
    def __init__(self,Node=None):
        if Node!=None:
            self.nodes=[Node]
        else:
            self.nodes=[]

    def printout(self):
        if isinstance(self.nodes[0],int) or isinstance(self.nodes[0],float):
            print [i for i in self.nodes]
        else:
            print [i.get_value() for i in self.nodes]

    def append_to_end(self,app):
        self.nodes.append(app)

    def extractmin(self):
        if len(self.nodes)==0:
            return None 
        out=self.nodes[0]
        self.nodes=self.nodes[-1:]+self.nodes[1:-1]
        self.heapify(0)
        return out

    def check_parent(self,loc=0):
        if loc==0:
            return True
        if loc%2: #odd
            p_index=loc/2
        else:
            p_index=loc/2-1
        if p_index<0:
            p_index=0
        if self.nodes[loc].get_value()<self.nodes[p_index].get_value():
            tmp=self.nodes[loc]
            self.nodes[loc]=self.nodes[p_index]
            self.nodes[p_index]=tmp
        self.check_parent(p_index)
        return

    def insert(self,value):
        self.append_to_end(value)
        self.check_parent(len(self.nodes)-1)
        return

    def heapify(self,index):
        while ((index+1)*2-1)<=(len(self.nodes)-1): #don't fall out of the array
            if ((index+1)*2)>len(self.nodes)-1:
                minc=(index+1)*2-1
            else:
                if isinstance(self.nodes[0],int) or isinstance(self.nodes[0],float):
                    child1=self.nodes[(1+index)*2-1]
                    child2=self.nodes[(index+1)*2]
                else: #Or maybe make a get_value in this class, inheriting objects
                    child1=self.nodes[(1+index)*2-1].get_value()
                    child2=self.nodes[(index+1)*2].get_value()
                if child1<child2: #repurposed to use values of objects if not int,float
                    minc=(index+1)*2-1
                else:
                    minc=(index+1)*2
            if self.nodes[index]>self.nodes[minc]:
                tmp=self.nodes[index]
                self.nodes[index]=self.nodes[minc]
                self.nodes[minc]=tmp
            index=minc
        return


