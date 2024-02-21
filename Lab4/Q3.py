from collections import deque

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

    def TSP(self):
        def tsp_bfs(start):
            queue = deque([(start, [start], 0)])
            min_distance = float('inf')
            min_path = []
            while queue:
                node, path, distance = queue.popleft()
                if len(path) == len(self.nodes): 
                    if distance < min_distance:
                        min_distance = distance
                        min_path = path
                for neighbor, weight in self.graph[node]:
                    if neighbor not in path:
                        new_path = path + [neighbor]
                        new_distance = distance + weight
                        queue.append((neighbor, new_path, new_distance))
            return min_distance, min_path

        min_distance = float('inf')
        min_path = []
        for node in self.nodes:
            distance, path = tsp_bfs(node)
            if distance < min_distance:
                min_distance = distance
                min_path = path

        print("Minimum distance for TSP using BFS:", min_distance)
        print("Path:", min_path)


def main():
    g1 = Graph()
    g1.connection("A","B",2)
    g1.connection("A","C",3)
    g1.connection("A","D",1)
    g1.connection("B","A",2)
    g1.connection("B","C",4)
    g1.connection("B","D",2)
    g1.connection("C","A",3)
    g1.connection("C","B",4)
    g1.connection("C","D",3)
    g1.connection("D","A",1)
    g1.connection("D","B",2)
    g1.connection("D","C",3)

    print("Solution:")
    g1.TSP()


if __name__ == "__main__":
    main()
