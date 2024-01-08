class Graph():
    def __init__(self):
        self.adj_matrix=[]
        self.adj_list={}
        self.nodes=[]
    def display(self):
        print("Adjacency Matrix:")
        print(self.adj_matrix)
        print("Adjacency List:")
        print(self.adj_list)
        print("Connections:")
        for i in self.nodes:
            for j in self.adj_list.get(i):
                print(f'({i}->{j[0]})',end=" ")
            print()
         
        
    def connection(self,origin,dest):
        if origin in self.adj_list:
            self.adj_list[origin].append(dest)
        else:
            self.adj_list[origin] = [dest]
        if dest in self.adj_list:
            self.adj_list[dest].append(origin)
        else:
            self.adj_list[dest] = [origin]
 

        self.nodes = sorted(list(self.adj_list.keys()))
        self.adj_matrix = [[0] * len(self.nodes) for _ in range(len(self.nodes))]
        
        for i in self.nodes:
            for j in self.adj_list.get(i):
                self.adj_matrix[self.nodes.index(i)][self.nodes.index(j)]=1


            

def main():
    g1=Graph()
    g1.connection('A','C')
    g1.connection('A','B')
    g1.connection('A','E')
    g1.connection('C','B')
    g1.connection('C','E')
    g1.connection('C','D')
    g1.connection('D','B')

    g1.display()


if __name__ == "__main__":
    main()
