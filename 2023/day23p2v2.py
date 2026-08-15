import time

starttime = time.time()

input_file = open("day23input.txt","r")
input_file = [list(i.strip()) for i in input_file.readlines()]

junctures = []
juncture_dict = {}

grid = {}

for i, r in enumerate(input_file):
    for j, c in enumerate(r):
        if c in ["^",">","<","v"]:
            grid[(i,j)] = "."
        else:
            grid[(i,j)] = c

neighbours = {}

for i, r in enumerate(input_file):
    for j, c in enumerate(r):
        if grid[(i,j)] == ".":
            neighbours[(i,j)] = []
            for n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if grid.get(n) == ".":
                    neighbours[(i,j)].append(n)
            if len(neighbours[(i,j)]) > 2:
                junctures.append((i,j))

start = [i for i in grid.keys() if grid[i] == "." and i[0] == 0][0]
dest = [i for i in grid.keys() if grid[i] == "." and i[0] == len(input_file)-1][0]

for junc in junctures + [start,dest]:
    paths = [[junc,i] for i in neighbours[junc]]
    final_paths = []
    while paths:
        new_paths = []
        for path in paths:
            if path[-1] in junctures or path[-1] in (start,dest):
                final_paths.append(path)
            else:
                next_step = [i for i in neighbours[path[-1]] if i not in path][0]
                new_paths.append(path+[next_step])
        paths = list(new_paths)
    juncture_dict[junc] = [(fp[-1],len(fp)-1) for fp in final_paths]

memo = {}

def DFS(node,path_so_far,rec_lev,record):
    if rec_lev <= 6:
        print(rec_lev)
    if node == dest:
        return 0
    if (node,path_so_far) in memo.keys():
        #print("MEMO USED")
        return memo[(node,path_so_far)]
    new_record = {v:list(k) for v,k in record.items()}
    for linked in new_record[node]:
        new_record[linked[0]].remove((node,linked[1]))
    try:
        return_val = max([n[1]+DFS(n[0],path_so_far.union(frozenset([n[0]])),rec_lev+1,new_record) for n in record[node]])
        memo[(node,path_so_far)] = return_val
        return return_val
    except: #all adjacent nodes are visited
        memo[(node,path_so_far)] = -1
        return -1
print(DFS(start,frozenset([start]),0,juncture_dict))

