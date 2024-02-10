class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        element = (priority, item)
        self.queue.append(element)
        self.queue.sort()

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0


class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = []

    def display(self):
        print("Adjacency List:")
        print(self.graph)
        print("Connections:")
        for i in self.nodes:
            for j in self.graph.get(i, []):
                print(f'({i}->{j[0]},{j[1]})', end=" ")
            print()

    def connection(self, origin, dest, weight):
        if origin in self.graph:
            self.graph[origin].append((dest, weight))
        else:
            self.graph[origin] = [(dest, weight)]
        if dest not in self.graph:
            self.graph[dest] = []

        self.nodes = list(self.graph.keys())  # Update nodes list
        self.adj_matrix = [[0] * len(self.nodes) for _ in range(len(self.nodes))]

        for i in self.nodes:
            for j in self.graph.get(i, []):
                self.adj_matrix[self.nodes.index(i)][self.nodes.index(j[0])] = j[1]

    def bfs(self, visited, queue,end,cost):
        if not queue.is_empty():
            weight, value = queue.dequeue()
            print(f'{value} ', end=" ")
            if value == end:
                print(f'\nCost:{cost+weight}')
                return True
            elif not self.graph[value]:
                return False



            for node in self.graph[value]:
                if node[0] not in visited:
                    visited.add(node[0])
                    queue.enqueue(node[0], node[1])
            self.bfs(visited, queue,end,cost+weight)

    def UniformCostSearch(self):
        visited = set()
        queue = PriorityQueue()
        queue.enqueue(0, 0)
        cost=0
        print("path from S to G -> ",end="")
        self.bfs(visited, queue,6,cost)


def main():
    g1 = Graph()
    g1.connection(0, 1, 2)
    g1.connection(0, 3, 5)
    g1.connection(1, 6, 1)
    g1.connection(2, 1, 4)
    g1.connection(3, 6, 6)
    g1.connection(3, 1, 5)
    g1.connection(4, 5, 3)
    g1.connection(4, 2, 4)
    g1.connection(5, 2, 6)
    g1.connection(5, 6, 3)

    print("Solution:")
    g1.UniformCostSearch()


if __name__ == "__main__":
    main()
