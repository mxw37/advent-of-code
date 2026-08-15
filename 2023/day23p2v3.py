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

paths = [[[start],0]]
finished_paths = []

while paths:
    print(paths)
    new_paths = []
    for path in paths:
        for dest_opt in juncture_dict[path[0][-1]]:
            if dest_opt[0] in path[0]:
                continue
            elif dest_opt[0] == dest:
                finished_paths.append([path[0]+[dest_opt[0]],path[1]+dest_opt[1]])
            else:
                new_paths.append([path[0]+[dest_opt[0]],path[1]+dest_opt[1]])
    paths = list(new_paths)

print(time.time()-starttime)
print(max([i[1] for i in finished_paths]))
