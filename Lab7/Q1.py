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
            if value not in visited:
                path = prev_path + [value]
                cost += path_cost
                if value == end:
                    print(f'\nCost: {cost}')
                    print("Path:", ' -> '.join(path))
                    return
                done=[]
                for node in self.graph[value]:
                    if node[0] not in done:
                        new_weight = node[1] +node[3]
                        queue.enqueue(node[0], new_weight, path,node[1])
                        done.append(node[0])
                visited.add(value)
                self.util(visited, queue, end, path,cost)


    def AStarSearch(self,start,goals):
        
        for goal in goals:
            visited = set()
            queue = PriorityQueue()
            queue.enqueue(start, 0)
            self.util(visited,queue,goal)


def main():
    g1 = Graph()
    g1.connection("A","B",6,10,8)
    g1.connection("A","F",3,10,6)
    g1.connection("B","D",2,8,7)
    g1.connection("B","C",3,8,5)
    g1.connection("C","D",1,5,7)
    g1.connection("C","E",5,5,3)
    g1.connection("D","E",8,7,3)
    g1.connection("E","I",5,3,1)
    g1.connection("E","J",5,3,0)
    g1.connection("F","G",1,6,5)
    g1.connection("F","H",7,6,3)
    g1.connection("G","I",3,5,1)
    g1.connection("H","I",2,3,1)
    g1.connection("I","J",3,1,0)
    

    print("\nSolution:")
    g1.AStarSearch("A",["J"])


if __name__ == "__main__":
    main()
