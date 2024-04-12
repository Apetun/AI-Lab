class Graph():
    def __init__(self):
        self.graph={}
        self.nodes=[]
        self.indegree=[]
        self.degree=[]
        
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
        self.indegree = [0]* len(self.nodes)
        self.degree = [0]* len(self.nodes)

        for node in self.nodes:
            if self.graph[node]:
                for neighbor in self.graph[node]:
                    self.indegree[self.nodes.index(neighbor)]+=1
        

    def bfs(self,visited,queue):
        if queue:
            temp=queue[0]
            queue.pop(0)
            for node in self.graph[temp]:
                
                self.degree[self.nodes.index(node)]+=1
                
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
            self.bfs(visited,queue)

    def is_cyclic(self,start):
        visited = set()
        queue = []

        queue.append(start)
        
        self.bfs(visited,queue)
        
        res = [item1 - item2 for item1, item2 in zip(self.degree,self.indegree)]

        return not all(ele == 0 for ele in res)




def main():
    g1=Graph()
    g1.connection(0,1)
    g1.connection(0,2)
    g1.connection(1,2)
    g1.connection(2,0)
    g1.connection(2,3)
    g1.connection(3,3)

    g1.display()
    print(f"is cyclic: {g1.is_cyclic(2)}")


if __name__ == "__main__":
    main()


