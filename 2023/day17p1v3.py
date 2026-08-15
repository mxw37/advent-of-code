import time

input_file = open("day17input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

options_dict ={("N",False):["N","E","W"],
               ("E",False):["N","S","E"],
               ("S",False):["S","E","W"],
               ("W",False):["N","S","W"],
               ("N",True):["E","W"],
               ("E",True):["N","S"],
               ("S",True):["E","W"],
               ("W",True):["N","S"]}
direct_dict = {"N":(-1,0),"E":(0,1),"S":(1,0),"W":(0,-1)}

grid = {}

for r, i in enumerate(input_file):
    for c, j in enumerate(i):
        grid[(r,c)] = int(j)

pq = {(0,0)}
visited = []

#Dict of (int,int) -> [int,list]
#1st item of list represents total heat loss of path
#2nd item of list is sublist represents last 3 moves of the shortest path/s to there
record = {(0,0):[0,[[]]]}
counter = 0

for i in range(0,len(input_file)):
    for j in range(0,len(input_file[0])):
        if i != 0 or j != 0:
            record[(i,j)] = [float("inf")]

def must_turn(path):
    if len(path) < 3:
        return False
    if path[-1] == path[-2] == path[-3]:
        return True
    return False

while pq:
    current_node = min(pq,key=lambda x:record[x][0])
    current_path = record[current_node]
    pq.remove(current_node)
    if current_node in visited:
        continue
    visited.append(current_node)
    total_options = set()
    for path in current_path[1]:
        if len(path) == 0:
            options = {"E","S"} #this assumes we start in top left corner
        else:
            options = options_dict[(path[-1],must_turn(path))]
        total_options = total_options.union(options)
    print(current_node)
    print(total_options)
    for option in total_options:
        direct = direct_dict[option]
        dest = (current_node[0]+direct[0],current_node[1]+direct[1])
        if dest in grid.keys():
            new_paths = []
            for path in current_path[1]:
                if len(path) == 0 or option in options_dict[(path[-1],must_turn(path))]:
                    new_paths.append(path + [option])
            if current_path[0]+grid[dest] < record[dest][0]:
                record[dest] = [current_path[0]+grid[dest],new_paths]
                pq.add(dest)
            elif current_path[0]+grid[dest] == record[dest][0]:
                record[dest][1].extend(new_paths)
                pq.add(dest)
                
    #print(pq)
    #print("\n")
    #print(record)

print(record[(len(input_file)-1,len(input_file[0])-1)])
