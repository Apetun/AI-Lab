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
        
    def dfs(self, node, visited, stack):
        visited.add(node)
        stack.append(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(node)
        return False

    def is_cyclic(self):
        visited = set()
        stack = []

        for node in self.nodes:
            if node not in visited:
                if self.dfs(node,visited,stack):
                    return True

        return False



def main():
    g1=Graph()
    g1.connection(0,1)
    g1.connection(0,2)
    g1.connection(1,2)
    g1.connection(2,0)
    g1.connection(2,3)
    g1.connection(3,3)

    g1.display()
    print(f"is cyclic: {g1.is_cyclic()}")


if __name__ == "__main__":
    main()


