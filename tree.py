class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.head = Node(None)
        
    def insert (self , value):

        if (self.head.data is None):
            self.head.data = value

        else:
            self.add(value , self.head)

    def add(self,value , node):
        
        if ( value < node.data):
            if (node.left is None):
                node.left = Node(value)
                
            else:
                self.add(value , node.left)
        else:
            if (node.right is None):
                node.right = Node(value)
            else:
                
                self.add(value,node.left)

    def search (self,value):

        if (self.head.data == value):
            print ("value found" + str(value))
            return self.head
        else:
            return self._search(value,self.head)
            
    def _search(self,val,node):
        if ( node.data == val):
            "print (""value found :"" + str(val))"
            return node

        else:
            if( node.data < val) and (node.right is not None):
                
                return self._search(val,node.right)
            elif ( node.data > val) and (node.left is not None):
                
                return self._search(val,node.left)
            else :
                print ("Value not found")
        
    def delete (self,value):
        Removnode = self.search(value) 
        hval = self.head
        
        
        if ( Removnode.left is None) & ( Removnode.right is None):
            if ( hval.data < Removnode.data):
                hval = hval.right
                self.delete(value)
            
            elif ( hval.data > Removnode.data):
                hval = hval.left
                self.delete(value)
            else:
                hval = None
        elif ( Removnode.left is None) & ( Removnode.right is not None):
            Removnode = Removnode.right
        elif ( Removnode.left is not None) & ( Removnode.right is  None):
            Removnode = Removnode.left
        
                    
    def treeprint (self):
        if(self.head != None):
            self._print(self.head)
    def _print (self,node):
        if (node != None):
            self._print(node.left)
            print (node.data),
            self._print(node.right)

    
                
            
tree = Tree()
tree.insert(12)
tree.insert(6)
tree.insert(3)
tree.insert(14)

tree.search(3)
tree.search(5)

tree.delete(3)
tree.treeprint()
