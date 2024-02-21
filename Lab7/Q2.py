class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority, prev_path=[],cost=0):
        element = (priority, item, prev_path,cost)
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
                print(f'({node}->{j[0]},{j[1]},{j[2]},{j[3]})', end=" ")
            print()

    def connection(self, origin, dest, pcost,hcostorigin,hcostdest):
        if origin in self.graph:
            self.graph[origin].append((dest, pcost,hcostorigin,hcostdest))
        else:
            self.graph[origin] = [(dest, pcost,hcostorigin,hcostdest)]
        if dest not in self.graph:
            self.graph[dest]=[]

        self.nodes = sorted(list(self.graph.keys()))

    def util(self, visited, queue, end, path=[],cost=0):
        if not queue.is_empty():
            weight, value, prev_path,path_cost = queue.dequeue()
            path = prev_path + [value]
            cost += path_cost
            if value == end:
                print(f'\nCost: {cost}')
                print("Path:", ' -> '.join(path))
                return
            for node in self.graph[value]:
                if node[0] not in visited:
                    new_weight = node[1] +node[3]
                    queue.enqueue(node[0], new_weight, path,node[1])
                    visited.add(node[0])
            print(queue.queue)
            self.util(visited, queue, end, path,cost)


    def AStarSearch(self,start,goals):
        
        for goal in goals:
            visited = set()
            queue = PriorityQueue()
            queue.enqueue(start, 0)
            print(f"\npath from {start} to {goal} -> ",end="")
            self.util(visited,queue,goal)


def main():
    g1 = Graph()
    g1.connection("S","A",5,5,7)
    g1.connection("S","B",9,5,3)
    g1.connection("S","D",6,5,6)
    g1.connection("A","G1",9,7,0)
    g1.connection("A","B",3,7,3)
    g1.connection("B","A",2,3,7)
    g1.connection("B","C",1,3,4)
    g1.connection("C","S",6,4,5)
    g1.connection("C","G2",5,4,0)
    g1.connection("C","F",7,4,6)
    g1.connection("D","C",2,6,4)
    g1.connection("D","E",2,6,5)
    g1.connection("D","S",1,6,5)
    g1.connection("E","G3",7,5,0)
    g1.connection("F","D",2,6,6)
    g1.connection("F","G3",8,6,0)

    g1.display()

    print("\nSolution:")
    g1.AStarSearch("S",["G1","G2","G3"])


if __name__ == "__main__":
    main()
