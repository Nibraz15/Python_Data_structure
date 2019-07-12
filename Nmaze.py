



def Nmaze(Maze):
    Size = len(Maze)
    end = (Size-1,Size-1)
    lastmov = ""
    Maze[0][0] = '*'
    i = 0
    j = 0
    
    while (i,j) != end:
        if(forward(i,j,Maze,Size)):
            j = j+1
            lastmov = "forward"
            Maze[i][j] = '*'
        elif (downward(i,j,Maze,Size)):
            i = i+1
            lastmov = "down"
            Maze[i][j] = '*'
        elif (left(i,j,Maze,Size)):
            j=j-1
            lastmov = "left"
            Maze[i][j] = '*'
        elif (up(i,j,Maze,Size)):
            i=i-1
            lastmov = "up"
            Maze[i][j] = '*'
        else:
            if (lastmov == "forward"):
                Maze[i][j] = 0
                j = j-1
                
            elif(lastmov == "down"):
                Maze[i][j] == 0
                i = i-1
            elif (lastmov == "left"):
                Maze[i][j] = 0
                j = j+1
                
            elif(lastmov == "up"):
                Maze[i][j] == 0
                i = i+1
    
    for i in range(Size):
        for j in range(Size):
            if Maze[i][j] != '*':
                Maze[i][j] = 0
            elif Maze[i][j] == '*':
                Maze[i][j] = 1
    for i in range(Size):
        print Maze[i]

def forward(i,j,Maze,Size):
    if j+1 < Size:
        if Maze[i][j+1] == 1:
            return True
    return False

def downward(i,j,Maze,Size):
    if i+1 < Size:
        if Maze[i+1][j] == 1:
            return True
    return False
                
def left(i,j,Maze,Size):
    if j-1 >= Size:
        if Maze[i][j-1] == 1:
            return True
    return False

def up(i,j,Maze,Size):
    if i-1 >= 0:
        if Maze[i-1][j] == 1:
            return True
    return False

Maz = [[1, 0, 0, 0],[1, 1, 1, 1],[0, 1, 0, 0],[1, 1, 1, 1]]

Nmaze(Maz)

