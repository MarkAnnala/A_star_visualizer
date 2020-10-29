def find_neigs(location, grid, xMax, yMax): 
    #print(location)
    neigs = []
    x = location[0]
    y=location[1]
    if y-1 > -1 and grid[x][y-1] == 0:
        neigs.append((x,y-1))
    if y+1 < yMax and grid[x][y+1] == 0: 
        neigs.append((x, y+1)) 
    if x-1 > -1 and grid[x-1][y] == 0: 
        neigs.append((x-1, y))
    if x+1 < xMax and grid[x+1][y] == 0: 
        neigs.append((x+1,y))
    return(neigs)

#manhattandistance for a grid, used for "cost" in a_Star
def manhattan (current, goal):
    return(abs(current[0]- goal[0]) + abs(current[1]-goal[1]))

def calculate_expand (frontierElem): 
    return (frontierElem[1] +frontierElem[2])

def aStar(grid, current, goal): 
    if current == goal:
        return []
    frontier = []
    visited = []
    expanded = None 
                    #current pos, cost, h = lenght to goal, path
    frontier.append((current, 0, manhattan(current, goal) , [] ))
    while len(frontier) > 0: 
        #take out a new expanded node from frontier with the lowest cost 
        newExp = True
        while newExp: 
            #print(len(frontier))
            #print(frontier)
            costs = list(map(calculate_expand, frontier))
            lowest = costs.index(min(costs))
            if frontier[lowest] not in visited:
                expanded = frontier[lowest]
                del frontier[lowest]
                newExp = False
            else:
                del frontier[lowest]
        visited.append(expanded)
        
        if expanded[0] == goal: 
            
            for node in expanded[3]:
                grid[node[0]][node[1]] = 2    
            return expanded[3]

        neigbours = find_neigs(expanded[0], grid, len(grid), len(grid))
        for neig in neigbours: 
            neigExist = 0
            k = 0
            for front in frontier: 
                if neig == front[0]:
                    cost = manhattan(current,neig)
                    if cost < front[1]:
                        neigExist = 1
                        del frontier[k] 
                    else: 
                        neigExist = 2
                    break
                k+= 1
            if neigExist == 0 or neigExist == 1:
                cost = manhattan(current,neig)
                h = manhattan(neig, goal)
                path = list(expanded[3])
                path.append(expanded[0])
                frontier.append((neig, cost, h, path))
    
            

   

#aStar(grid = None, current =(1,1), goal=(2,2))