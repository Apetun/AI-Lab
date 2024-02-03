class Graph():
    def __init__(self):
        self.graph={}
        self.nodes=[]
        self.indegree=[]
    def display(self):
        print("Adjacency List:")
        print(self.graph)
        print(self.indegree)
    def connection(self,origin,dest):
        if origin in self.graph:
            self.graph[origin].append(dest)
        else:
            self.graph[origin] = [dest]

        if dest not in self.graph:
            self.graph[dest]=[]
            
        self.nodes = sorted(list(self.graph.keys()))
        self.indegree = [0]* len(self.nodes)

        for node in self.nodes:
            if self.graph[node]:
                for neighbor in self.graph[node]:
                    self.indegree[self.nodes.index(neighbor)]+=1


    

    def bfs(self,visited,queue):
        if queue:
            temp=queue[0]
            print(temp,end=" ")
            queue.pop(0)
            for node in self.graph[temp]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
            self.bfs(visited,queue)
            
        


    
    def topologicalOrder(self):
        visited = set() 
        queue = []

        for node in self.nodes:
            if self.indegree[self.nodes.index(node)]==0:
                queue.append(node)
        print(queue)
        self.bfs(visited,queue)




            

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
