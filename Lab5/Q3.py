class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority, prev_path=[]):
        element = (priority, item, prev_path)
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

    def util(self, visited, queue, end, path=[]):
        if not queue.is_empty():
            weight, value, prev_path = queue.dequeue()
            path = prev_path + [value]
            if value == end:
                print(f'\nCost: {weight}')
                print("Path:", ' -> '.join(path))
                return
            for node in self.graph[value]:
                if node[0] not in visited:
                    visited.add(node[0])
                    new_weight = node[1] + weight
                    queue.enqueue(node[0], new_weight, path)
            self.util(visited, queue, end, path)


    def UniformCostSearch(self,start,goals):
        
        for goal in goals:
            visited = set()
            queue = PriorityQueue()
            queue.enqueue(start, 0)
            print(f"\npath from {start} to {goal} -> ",end="")
            self.util(visited,queue,goal)


def main():
    g1 = Graph()
    g1.connection("Maldon","Tiptree",8)
    g1.connection("Tiptree","Clacton",29)
    g1.connection("Tiptree","Feering",3)
    g1.connection("Feering","Maldon",11)
    g1.connection("Feering","Blaxhall",46)
    g1.connection("Clacton","Maldon",40)
    g1.connection("Clacton","Harwich",17)
    g1.connection("Harwich","Triptree",31)
    g1.connection("Harwich","Blaxhall",40)
    g1.connection("Harwich","Dunwich",53)
    g1.connection("Blaxhall","Dunwich",15)
    g1.connection("Dunwich","Blaxhall",17)
    

    print("Solution:")
    g1.UniformCostSearch("Maldon",{"Dunwich"})


if __name__ == "__main__":
    main()
