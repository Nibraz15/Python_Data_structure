class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

class Dlinkedlist:
    def __init__(self):
        self.headval=None

    def push(self, NewVal):
        
        if (self.headval is None):
        
            self.headval = Node(NewVal)
        else:
            hval = self.headval
            Newnode = Node(NewVal)
            Newnode.nextval = self.headval
            self.headval.prevval = Newnode
            self.headval = Newnode

    def insertpos(self, Insval , pos):
        hval = self.headval
        Insnode = Node(Insval)
      
        if (pos == 1):
            Insnode.nextval = self.headval
            self.headval.prevval = Insnode
            self.headval = Insnode
        else:
            
            for i in range(2,pos):
                if (hval is not None):
                    hval = hval.nextval
                else:
                    print ("Index out of range")
            nextnode = hval.nextval
            Insnode.nextval = nextnode
            Insnode.prevval = hval
            hval.nextval = Insnode
            nextnode.prevval = Insnode

    def insertkey (self,prev,Insval):
        hval = self.headval
        Insnode = Node(Insval)
        if (hval is None):
            print ("Emplty list")
        else:
            while (hval.dataval != prev):
                if (hval is not None):
                    hval = hval.nextval
                else:
                    print ("Node is not in the list")
            nextnode = hval.nextval
            Insnode.nextval = nextnode
            Insnode.prevval = hval
            hval.nextval = Insnode
            nextnode.prevval = Insnode

    def remove (self,remov):
        hval = self.headval
        if (hval is None):
            print ("Emplty list")
        else:
            while (hval.dataval != remov):
                if (hval is not None):
                    hval = hval.nextval
                else:
                    print ("Node is not in the list")
            nextnode = hval.nextval
            hval = hval.prevval
            nextnode.prevval = hval
            hval.nextval = nextnode
    def listprint (self):
        while(self.headval is not None):
            print (self.headval.dataval)
            self.headval = self.headval.nextval


list1 = Dlinkedlist()
list1.push(1)
list1.push(2)
list1.push(10)
list1.push(13)
list1.insertpos(15,1)
list1.insertpos(4,4)
list1.insertkey(2,20)
list1.remove(2)
list1.listprint()

            
