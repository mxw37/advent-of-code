input_file = open("day23input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

grid = {}

for i, r in enumerate(input_file):
    for j, c in enumerate(r):
        grid[(i,j)] = c

paths = [[(0,1)]]
lengths = []

slopes_dict = {"^":(-1,0),"v":(1,0),"<":(0,-1),">":(0,1)}
forbidden_entry = {"^":(1,0),"v":(-1,0),"<":(0,1),">":(0,-1)}

while paths:
    #print(paths)
    new_paths = []
    for path in paths:
        location = grid[path[-1]]
        if path[-1][0] == len(input_file)-1:
            lengths.append(len(path))
        else:
            if location in slopes_dict.keys():
                options = [slopes_dict[location]]
            else:
                options = [(1,0),(-1,0),(0,-1),(0,1)]
            for option in options:
                dest = (path[-1][0] + option[0],path[-1][1] + option[1])
                if dest not in grid.keys():
                    continue
                elif dest in path or grid[dest] == "#":
                    continue
                elif grid[dest] in slopes_dict.keys():
                    if option != forbidden_entry[grid[dest]]:
                        new_paths.append(path+[dest])
                elif grid[dest] == ".":
                    new_paths.append(path+[dest])
                else:
                    raise Exception("unknown character")
    paths = list(new_paths)

print(max(lengths)-1)
