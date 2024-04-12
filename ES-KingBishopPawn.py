class KingBishopPawn:
    def __init__(self,kpos,bpos,ppos):
        self.board = [[0]*8 for _ in range(8)]
        self.kpos=kpos
        self.bpos=bpos
        self.ppos=ppos
        self.invalid = self.calinvalid(bpos,ppos)
        self.moves= [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
        
    def heuristic(self,cord):
        x,y=cord
        return (7-x)+(7-y)
        
    def moveK(self,cord,direction):
        k = cord
        k = (k[0]+direction[0],k[1]+direction[1])
        if self.checkvalid(k) and k not in self.invalid:
            return True
        return False
                    
        
    def dfs(self, cord, stack, visited):
        print("Current position:", cord)
        
        self.display(cord)
        
        if cord == (7, 7):
            stack.append(cord)
            return True
        
        visited.append(cord)  
        
        nextmoves = []
        for move in self.moves:
            if self.moveK(cord, move):
                next_pos = (cord[0] + move[0], cord[1] + move[1])
                if next_pos not in visited:
                    nextmoves.append(next_pos)
        
        if nextmoves:
            print("Next moves:", nextmoves)
        else:
            print("Backtracking")
            
        for next_pos in nextmoves:
            if self.dfs(next_pos, stack + [next_pos], visited.copy()): 
                return True
        
        return False
       

            
       
    
            
    def solve(self):
        stack = []
        visited = []
        
        if self.dfs(self.kpos,stack,visited):
            print(stack)
            for cord in stack:
                self.kpos = cord
                self.display()
        else:
            print("Not solvable")
            
            
    def solveUCS(self):
        queue = []
        visited = []
        queue+=[(self.heuristic(self.kpos),self.kpos,[])]
        self.UCS(queue, visited)
        
        
        
        
    def UCS(self, queue, visited):
        if queue:
            weight,cord,path = queue.pop(0)
            
            print("Current position:", cord)
            self.display(cord)
            path = path+[cord]
            
            if cord == (7, 7):
                print(path)
                return True
            
            visited.append(cord)  
            
            nextmoves = []
            for move in self.moves:
                if self.moveK(cord, move):
                    next_pos = (cord[0] + move[0], cord[1] + move[1])
                    if next_pos not in visited:
                        nextmoves.append((weight+self.heuristic(next_pos),next_pos))
            
            if nextmoves:
                nextmoves.sort()
                print("Next moves:",nextmoves)          
            else:
                print("Backtracking")
                
            for next_pos in nextmoves:
                w,cord = next_pos
                if self.UCS(queue+[(w+weight,cord,path)], visited.copy()): 
                    return True
            
            return False 
        return False   
        
    
    
        
    def calinvalid(self,bpos,ppos):
        invalid = []
        invalid+=[bpos,ppos]
        b = bpos
        for i in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            b=(b[0]+i[0],b[1]+i[1])
            while self.checkvalid(b):
                invalid+=[b]
                b=(b[0]+i[0],b[1]+i[1])
            b = bpos
        
        invalid+=[(ppos[0]+1,ppos[1]+1),(ppos[0]+1,ppos[1]-1)]
        
        return invalid     

        
    def display(self,kpos):
        for i in range(8):
            line = "|"
            for j in range(8):
                if (i,j) == kpos:
                    line+="K|"
                elif (i,j) == self.bpos:
                    line+="B|"
                elif (i,j) == self.ppos:
                    line+="P|"
                elif (i,j) in self.invalid:
                    line+="x|"
                else:
                    line+=".|"
            print(line)        
        
        
    def checkvalid(self,cord):
        x,y=cord
        if 0<= x <8 and 0<=y<8:
            return True
        else:
            return False
        
    
if __name__== "__main__" :
     game=KingBishopPawn((1,1),(2,3),(3,4))
     game.solveUCS()
     
    
    
        