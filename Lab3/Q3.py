class Maze():
    def __init__(self):
        self.graph={}
        self.nodes=[]
    def display(self):
        print("Adjacency List:")
        print(self.graph)
        
    def connection(self,origin,dest):
        if origin in self.graph:
            self.graph[origin].append(dest)
        else:
            self.graph[origin] = [dest]

        if dest not in self.graph:
            self.graph[dest]=[]
            
        self.nodes = sorted(list(self.graph.keys()))

    
    def dfs(self,node,visited, stack,end):
    	
        if node == end:
            stack.append(node)
            print(stack)
            return True
        elif not self.graph[node]:
            return False
            	
        if node not in visited:
            visited.add(node)        
            for neighbour in self.graph[node]:
                if self.dfs(neighbour,visited,stack+[node],end):                    
                    return True    
       
    
    def solve(self,start,ends):
        
        for end in ends:
            visited = set() 
            stack = []
            self.dfs(start,visited,stack,end)
                    




            

def main():
    g1=Maze()
    g1.connection(20,15)
    g1.connection(15,10)
    g1.connection(10,9)
    g1.connection(10,5)
    g1.connection(5,4)
    g1.connection(9,14)
    g1.connection(14,13)
    g1.connection(14,19)
    g1.connection(19,18)
    g1.connection(18,17)
    g1.connection(17,16)
    g1.connection(17,12)
    g1.connection(12,11)
    g1.connection(11,6)
    g1.connection(6,1)
    g1.connection(1,2)
    g1.connection(2,3)
    g1.connection(3,8)
    g1.connection(8,7)
    
    print("Adjacency list of the maze:")
    g1.display()
    print("All solutions:")
    g1.solve(20,[2,5])


if __name__ == "__main__":
    main()