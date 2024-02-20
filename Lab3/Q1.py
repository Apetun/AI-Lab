class Graph():
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

    

    def dfs(self,node,visited, stack):
        if node not in visited:
            visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour,visited,stack)
            stack.append(node)
        


    
    def topologicalOrder(self):
        visited = set() 
        stack = []

        for node in self.nodes:
            if node not in visited:
                self.dfs(node, visited, stack)
                    

        print(stack[::-1])



            

def main():
    g1=Graph()
    g1.connection(5,0)
    g1.connection(5,2)
    g1.connection(4,0)
    g1.connection(4,1)
    g1.connection(2,3)
    g1.connection(3,1)

    g1.display()
    print("Topological Order :")
    g1.topologicalOrder()


if __name__ == "__main__":
    main()
