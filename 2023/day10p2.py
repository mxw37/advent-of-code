#rank 653
input_file = open("day10input.txt","r")

grid = []

for i in input_file:
    grid.append(list(i.strip()))

def get_dest(now, last): #now and last are coordinates
    options = []
    pipe_type = grid[now[0]][now[1]]
    north = [now[0]-1,now[1]]
    south = [now[0]+1,now[1]]
    east = [now[0],now[1]+1]
    west = [now[0],now[1]-1]
    if pipe_type == "|":
        options = [north,south]
    if pipe_type == "-":
        options = [east,west]
    if pipe_type == "L":
        options = [north,east]
    if pipe_type == "J":
        options = [north,west]
    if pipe_type == "7":
        options = [south,west]
    if pipe_type == "F":
        options = [south,east]
    return [i for i in options if i != last][0]

def find_S(lst):
    return_val = []
    for i in range(0,len(lst)):
        if "S" in lst[i]:
            return_val.append(i)
            break
    for j in range(0,len(lst[0])):
        if lst[return_val[0]][j] == "S":
            return_val.append(j)
            break
    return return_val

start = find_S(grid)

current = [start[0]-1,start[1]] #This was hardcoded by checking the input to see which pipes linked to S
last = start

steps = 1

while current != start:
    print(current)
    steps += 1
    current, last = get_dest(current, last), current

print(current)
