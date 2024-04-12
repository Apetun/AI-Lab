class Sudoku:
    def __init__(self):
        self.grid=[[0]*9 for _ in range(9)]
        
    def display(self):
        print("-" * 21)
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(self.grid[i][j], end=" ")
            print()
        print("-" * 21)

        
    def connection(self,cord,value):
        x,y=cord
        self.grid[x][y] = value
    
    def check(self,cord,value):
        
        x,y=cord
        
        if value in self.grid[x]:
            return False
    
   
        for i in range(9):
            if self.grid[i][y] == value:
                return False
    
    
        start_row, start_col = 3 * (x // 3), 3 * (y // 3)
        
        for i in range(3):
            for j in range(3):
                if self.grid[start_row+i][start_col+j] == value:
                    return False
    
        return True
    
    
    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return -1, -1
    
    def dfs(self):
        x,y = self.find_empty_location()
        
        if x==-1 and y==-1:
            return True
        for num in range (1,10):
            if self.check((x,y),num):
                self.grid[x][y]=num
                if self.dfs():
                    return True        
                self.grid[x][y]=0
        
        return False
        
    def solve(self):
        if self.dfs():
            print("Solved")
        else:
            print("Unsolvable")    
        
        
if __name__=="__main__":
    game = Sudoku()
    initial_state = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    game.grid = initial_state
    print("Intial State:")
    game.display()
    game.solve()
    game.display()
    
    