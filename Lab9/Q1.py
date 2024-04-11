
start = (0,0)
goal = (2,0)

rules = {
    1: lambda x, y: (4, y) if x < 4 else None,
    2: lambda x, y: (x, 3) if y < 3 else None,
    3: lambda x, y: (0, y) if x > 0 else None,
    4: lambda x, y: (x, 0) if y > 0 else None,
    5: lambda x, y: (4, y-(4-x)) if x + y >= 4 and y > 0 else None,
    6: lambda x, y: (x-(3-y), 3) if x + y >= 3 and x > 0 else None,
    7: lambda x, y: (x+y, 0) if x + y <= 4 and y > 0 else None,
    8: lambda x, y: (0, x+y) if x + y <= 3 and x > 0 else None,
    9: lambda x, y: (2, 0) if x == 0 and y == 2  else None,
}

def bfssearch(start,goal,iter = 0):
        
            x,y = start
            neighbours = [] 
            for rule in rules.keys():
                temp = rules[rule](x,y)
                if temp!=None:
                    neighbours.append(temp)
            if not neighbours:
                return False
            if goal in neighbours:
                return True
            for neighbour in neighbours:
                if bfssearch(neighbour,goal,iter=iter+1):
                    print(neighbour)
                    return True
            return False


def solve(start,goal):
    visited=[]
    if bfssearch(start,goal):
        print(start)

    


solve(start,goal)