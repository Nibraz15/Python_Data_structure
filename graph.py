class Node:
    def __init__(self,value = None):
        self.value = value
        self.neighbourli = []
        self.neigh = {}
        self.color= "white"
        self.parent = None
        self.distance = 10000
        self.parentlist = []
        self.childlist = []
        self.findtime =0
        self.completetime =0

    
    def neighbour(self,neigh={}):
        self.neigh = neigh

class Graph:

  
    vertices = []
    visited = []
    
    def addvertices(self,vertex):
        if len(self.vertices) == 0:
            newvert = Node(vertex)
            self.vertices.append(newvert)
        else:

            for i in self.vertices:
                if i.value != vertex:
                    newvert = Node(vertex)
                    self.vertices.append(newvert)
                    return True
                else:
                    return False
    def addedges(self,v,u,weight=1):
        for i in self.vertices:
            if i.value == v:
                for j in self.vertices:
                    if j.value == u:
                        i.neigh[j]= weight;
                        i.neighbourli.append(j.value) 
                        j.neigh[i] = weight;
                        j.neighbourli.append(i.value) 
                        return True
                        break
                break
    def search(self,u):
        h = False
        for i in self.vertices:
            if i.value == u:
                h= True
        return h

    def printchild(self,u):
        v=self.nodere(u)
        for i in v.childlist:
            print (i.value),
        print (" ")
    
    def printparent(self,u):
        v=self.nodere(u)
        
        for i in v.parentlist:
            print (i.value) ,
        print (" ")

    def nodere(self,u):
        for i in self.vertices:
            if i.value == u:
                return i 
    def findpath(self,u,v):
        if (self.search(u) & self.search(v)):
            self.bfs(self.nodere(u))
            self.traverse(self.nodere(v))

    def dfs(self,vertex):
        global time
        time = 1
        vertex = self.nodere(vertex)
        self._dfs(vertex)
    
    def _dfs(self,vertex):
        global time
        vertex.color = "red"
        vertex.findtime = time
        vertex.neighbourli.sort()
        time +=1
        for i in vertex.neighbourli:
            if self.nodere(i).color == "white":
                self._dfs(self.nodere(i))
        vertex.color = "blue"
        vertex.completetime = time
        time +=1


    def dijkstar (self,start):
        start = self.nodere(start)
        start.distance = 0
        self._dijkstar(start)
        self.visited = []

    def _dijkstar(self,start):
        
        start.neighbourli.sort()
        for i in start.neighbourli:
            if ((i,start.value) not in self.visited) and ((start.value,i) not in self.visited):
                
                dis = start.distance + start.neigh[self.nodere(i)]
                print dis
                if self.nodere(i).distance > dis:
                    
                    self.nodere(i).distance = dis
                    self.nodere(i).parent = start
                self.visited.append((i,start.value))
                self.visited.append((start.value,i))
            
        start.color = "red"
        
        for j in start.neighbourli:
            if self.nodere(j).color != "red":
                self._dijkstar(self.nodere(j))
                
    def mst(self,vertex):
        

    
    def bfs(self,u):
        u.distance = 0
        vert = []
        vert.insert(0,u)
        while(len(vert)>0):
            current = vert.pop()
            for nbr in current.neigh:
                if nbr.color == "white" :
                    nbr.color = "gray"
                    nbr.distance = nbr.distance + current.neigh[nbr]
                    nbr.parent = current
                    vert.insert(0,nbr)
            current.color = "black"
    def traverse(self,v):
        x=v
        path = []
        dista = x.distance
        
        while (x.parent != None):
            path.insert(0,x.value)
            x = x.parent
        path.insert(0,x.value)
        print (path,dista)
    
    def findAll(self,u,v):
        if (self.search(u) & self.search(v)):
            self._findAll(self.nodere(u),self.nodere(v))
            return self.find_all_paths(self.nodere(u),self.nodere(v))
    
    def _findAll(self,u,v):

        for i in u.neigh:
            if i.color == "white":
                i.distance = u.distance +1 

            if i!=v:
                if (i not in u.parentlist and i.distance > u.distance)  :
                    if i not in u.childlist:
                        u.childlist.append(i)
                    i.parentlist.append(u)
                    
                    u.color = "grey"
                    self._findAll(i,v)
                     
                elif i not in u.parentlist and i.distance < u.distance :
                    if u not in i.childlist:
                        i.childlist.append(u)
                    u.parentlist.append(i)
                    
                    
            elif (i ==v) and (i not in u.childlist):
                u.childlist.append(i)
                if u not in i.parentlist:
                    i.parentlist.append(u)
                break
                
            
        if(len(u.childlist) != 0):
            for x in u.childlist:
                if (len(x.childlist) ==0) and x!=v :
                    u.childlist.remove(x) 
        u.parentlist = list(set(u.parentlist))

    def find_all_paths(self,start, end, path=[]):
        path = path + [start.value]
        if start == end:
            
            return [path]
       
        paths = []
        for node in start.neigh:
            if node.value not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        
        return paths
                          
        

    def printvert(self):
        for i in self.vertices:
            if i.parent == None:
                print (i.value), i.parent , i.distance
            else:
                print (i.value), i.parent.value , i.distance

        print ("")
    
    def printedge(self,vertex):
        for i in self.vertices:
            if i.value == vertex:
                for j in i.neigh:
                    print (str(i.value)+" "+str(j.value)+":"+str(i.neigh[j]))
                break

def Kniht(Bdsize):
    Kngaph = Graph()
    for row in range (Bdsize):
        for col in range(Bdsize):
            currentpos = NodePos(row,col,Bdsize)
            Kngaph.addvertices(currentpos)
    for row in range (Bdsize):
        for col in range(Bdsize):
            currentpos = NodePos(row,col,Bdsize)
            leagal = getLegal(row,col,Bdsize)
        
            
            i = 0
            while (len(leagal)>i):
                Value = leagal[i]
                Kngaph.addedges(currentpos,Value)
                i= i+1
    return Kngaph

def KnightTour(n,path,u,limit):
    
    u.color = "grey"
    path.append(u.value)
    if n<limit:
        x = oderbyAvail(u)
        done = False
        for i in x:
            if i.color == "white":
                done = KnightTour(n+1,path,i,limit)
        if not done:
            path.pop()
            u.color = "white"
    else:
        done = True
    return done

def NodePos (r,w,N):
    return (r*N) + w

def oderbyAvail (n):
    resList=[]
    for v in n.neigh:
        if v.color == "white":
            c = 0
            for w in v.neigh:
                if w.color == "white":
                    c = c+1
            resList.append((c,v))
    resList.sort(key=lambda x:x[0])
    return [y[1] for y in resList]


def getLegal(r,c,N):
    legal = []
    if (r+2 < N) & (c+1 < N) :
        Mov1 = NodePos(r+2,c+1,N)
        legal.append(Mov1)
    if (r+2 < N) & (c-1 >= 0 ) :
        Mov2 = NodePos(r+2,c-1,N)
        legal.append(Mov2)
    if (r-2 >= 0) & (c+1 < N) :
        Mov3 = NodePos(r-2,c+1,N)
        legal.append(Mov3)
    if (r-2 >= 0) & (c-1 >= 0) :
        Mov4 = NodePos(r-2,c-1,N)
        legal.append(Mov4)
    if (r+1 < N) & (c+2 < N) :
        Mov5 = NodePos(r+1,c+2,N)
        legal.append(Mov5)
    if (r-1 >= 0) & (c+2 < N ) :
        Mov6 = NodePos(r-1,c+2,N)
        legal.append(Mov6)
    if (r+1 < N) & (c-2 >= 0) :
        Mov7 = NodePos(r+1,c-2,N)
        legal.append(Mov7)
    if (r-1 >= 0) & (c-2 >= 0) :
        Mov8 = NodePos(r-1,c-2,N)
        legal.append(Mov8)
    return legal


graph1 = Graph()

graph1.addvertices(1)
graph1.addvertices(2)
graph1.addvertices(3)
graph1.addvertices(4)
graph1.addvertices(5)
graph1.addvertices(6)
graph1.addvertices(7)

graph1.addedges(1,2)
graph1.addedges(1,3)
graph1.addedges(1,4)
graph1.addedges(2,5)
graph1.addedges(3,6)
graph1.addedges(1,6)
graph1.addedges(2,7)
graph1.addedges(3,7)
graph1.addedges(2,3)



graph1.dijkstar(1)
print (graph1.vertices)
