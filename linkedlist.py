class Node:
  def __init__(self,dataval=None):
    self.dataval=dataval
    self.nextval=None

class Slinkedlist:
  def __init__(self):
    self.headval=None
  
  def listprint(self):
    printval = self.headval
    while printval is not None:
      print (printval.dataval)
      printval= printval.nextval
   
  def Atbeg(self,newdata):
    Newnode = Node(newdata)
    Newnode.nextval = self.headval
    self.headval = Newnode
  
  def Atend(self,newdata):
    Newnode = Node(newdata)
    node = self.headval
    while node.nextval is not None:
      node = node.nextval
    node.nextval = Newnode
  
  def Atmid(self,newdata,pos):
    Newnode =Node(newdata)
    node = self.headval
    for i in range (2,pos):
      node = node.nextval
    node1 = node.nextval
    
    Newnode.nextval = node1
    node.nextval = Newnode
    
  def Rem (self,removekey):
    Removenode= Node(removekey)
    hval = self.headval
    
    if (hval.dataval is None):
      Return ("Empty List")
    
    elif (hval.dataval == Removenode.dataval):
      hval = hval.nextval
      self.headval = None
      self.headval = hval
    
    else :
      prev = hval
      hval = hval.nextval
      while (hval.dataval != removekey ):
        hval = hval.nextval
        prev = prev.nextval
      prev.nextval = hval.nextval
        

list1 = Slinkedlist()
list1.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node ("Thu")

list1.headval.nextval = e2
e2.nextval =e3
e3.nextval=e4

list1.Atbeg("Sun")
list1.Atend("Fri")
list1.Atmid("Sat",7)

list1.Rem("Sun")
list1.listprint()