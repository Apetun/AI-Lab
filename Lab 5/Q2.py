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
        print(self.nodes)
        print("Connections:")
        for node in self.nodes:
            for j in self.graph.get(node):
                print(f'({node}->{j[0]},{j[1]})', end=" ")
            print()

    def connection(self, origin, dest, weight):
        if origin in self.graph:
            self.graph[origin].append((dest, weight))
        else:
            self.graph[origin] = [(dest, weight)]
        if dest not in self.graph:
            self.graph[dest] = []

        self.nodes = sorted(list(self.graph.keys()))

    def bfs(self, visited, queue,end,cost):
        if not queue.is_empty():
            weight, value = queue.dequeue()
            print(f'{value} ', end=" ")
            if value == end:
                print(f'\nCost:{cost+weight}')
                return
            for node in self.graph[value]:
                if node[0] not in visited:
                    visited.add(node[0])
                    queue.enqueue(node[0], node[1])
            self.bfs(visited, queue,end,cost+weight)

    def UniformCostSearch(self):
        
        goals = {"G1","G2","G3"}
        for goal in goals:
            visited = set()
            queue = PriorityQueue()
            queue.enqueue("S", 0)
            cost=0
            print(f"\npath from S to {goal} -> ",end="")
            self.bfs(visited,queue,goal,cost)


def main():
    g1 = Graph()
    g1.connection("S","A",5)
    g1.connection("S","B",9)
    g1.connection("S","D",6)
    g1.connection("A","B",3)
    g1.connection("A","G1",9)
    g1.connection("B","A",2)
    g1.connection("B","C",1)
    g1.connection("C","F",7)
    g1.connection("C","S",6)
    g1.connection("C","G2",5)
    g1.connection("D","C",2)
    g1.connection("D","E",2)
    g1.connection("E","G3",7)
    g1.connection("F","D",2)
    g1.connection("F","G3",8)

    print("Solution:")
    g1.display()
    g1.UniformCostSearch()


if __name__ == "__main__":
    main()
