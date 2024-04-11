
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

def dfssearch(stack,visited,goal):
        
        if stack:
            x,y = stack[-1]
            visited.append((x,y))
            for rule in rules.keys():
                temp = rules[rule](x,y)
                if(temp!=None):
                    if temp == goal:
                        stack.append(temp)
                        return
                    if temp not in visited:
                        stack.append(temp)
                    dfssearch(queue,visited,goal)
            stack.pop[-1]


def solve(start,goal):
    stack=[start]
    visited=[]
    path = []
    if dfssearch(queue,visited,goal):
        print(start)

    


solve(start,goal)