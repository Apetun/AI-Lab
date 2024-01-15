class Graph():
    def __init__(self):
        self.adj_list={}
        self.nodes=[]
    def display(self):
        print("Adjacency List:")
        print(self.adj_list)
        
    def connection(self,origin,dest):
        if origin in self.adj_list:
            self.adj_list[origin].append(dest)
        else:
            self.adj_list[origin] = [dest]

        if dest not in self.adj_list:
            self.adj_list[dest]=[]
            
        self.nodes = sorted(list(self.adj_list.keys()))
        
    def util(self,i,visited,stack):
        
        visited[self.nodes.index(i)] = True
        
        for neighbor in self.adj_list[i]:
            if not visited[self.nodes.index(neighbor)]:
                self.util(neighbor, visited, stack)
        stack.append(i)
    
    def topologicalOrder(self):
        visited = [False] * len(self.nodes)
        stack = []

        for i in range(len(self.nodes)):
            if not visited[i]:
                self.util(self.nodes[i], visited, stack)
                    

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
    g1.topologicalOrder()


if __name__ == "__main__":
    main()
