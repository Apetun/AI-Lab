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
        
    def util(self, i, visited, stack):
        visited[self.nodes.index(i)] = True
        stack[self.nodes.index(i)] = True

        for neighbor in self.adj_list[i]:
            if not visited[neighbor]:
                if self.util(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True

        stack[self.nodes.index(i)] = False
        return False

    def is_cyclic(self):
        visited = [False] * len(self.nodes)
        stack = [False] * len(self.nodes)

        for i in range(len(self.nodes)):
            if not visited[i]:
                if self.util(self.nodes[i], visited,stack):
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


