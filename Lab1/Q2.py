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
    def connection(self,origin,dest,weight):
        if origin in self.adj_list:
            self.adj_list[origin].append([dest,weight])
        else:
            self.adj_list[origin] = [[dest,weight]]
        if dest not in self.adj_list:
            self.adj_list[dest]=[]


        self.nodes = sorted(list(self.adj_list.keys()))
        self.adj_matrix = [[0] * len(self.nodes) for _ in range(len(self.nodes))]
        
        for i in self.nodes:
            for j in self.adj_list.get(i):
                self.adj_matrix[self.nodes.index(i)][self.nodes.index(j[0])]=j[1]


            

def main():
    g1=Graph()
    g1.connection(1,2,1)
    g1.connection(1,3,1)
    g1.connection(2,3,3)
    g1.connection(3,4,4)
    g1.connection(4,1,5)

    g1.display()


if __name__ == "__main__":
    main()
