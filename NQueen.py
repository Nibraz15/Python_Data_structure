
def NQueen(Bsize):
    Mat = _NQueen(Bsize)

    for i in range (Bsize):
        print Mat[i]

def _NQueen(Bsize):
    Board = []
    for i in range (Bsize):
        Board.append([])
    for i in range (Bsize):
        for j in range (Bsize):
            Board[i].append(0)
    row = 0
    while row < Bsize:
        if (add(row,Bsize,Board)):
            
            row = row+1
        else:
            row = row-1
    return Board
def add(row,Bsize,Board):
    if 1 in Board[row]:
        x = Board[row].index(1)
        Board[row][x] = 0
        if x+1<Bsize:
            for i in range(x+1,Bsize):
                if(addable(row,i,Bsize,Board)):
                    Board[row][i] = 1
                    return True
        else:
            return False
    else:
        for i in range(Bsize):
            if(addable(row,i,Bsize,Board)):
                    
                    Board[row][i] = 1
                    
                    return True
        return False
        

    
        
def addable (r,c,N,Brd):

    
    for i in range (N):
        if Brd[i][c] == 1:
            
            return False
    
    y = c

    for i in range(r,0,-1):
        if (y-1 >= 0):
            y=y-1
            if Brd[i-1][y] == 1 :
                
                return False
               
    
    x = c
    for i in range(r,0,-1):
        if (x+1 < N):
            x=x+1
            if Brd[i-1][x] == 1:
                
                return False
                
    c1 = c
    c2 = c
    for i in range(r+1,N):
     
               
        if (c2+1 < N):
            c2 = c2+1
            if Brd[i][c2] == 1:
                
                return False
                
    return True


NQueen(16)






