input_file = open("day23input.txt","r")
input_file = [list(i.strip()) for i in input_file.readlines()]

#surround grid in # to avoid requiring bounds checking
input_file = [["#"] + i + ["#"] for i in input_file]
input_file.insert(0,["#"]*len(input_file[0]))
input_file.append(["#"]*len(input_file[0]))

paths = [[(1,2)]]
lengths = []

directions = {"^":(1,0),"v":(-1,0),"<":(0,-1),">":(0,1)}

while paths:
    new_paths = []
    print("STARTING ITERATION")
    for path in paths:
        print("NEXT PATH = " + str(path))
        last_step = path[-1]
        last_pos = input_file[last_step[0]][last_step[1]]
        if last_pos in directions.keys():
            print("SLOPE")
            next_step = (last_step[0]+directions[last_pos][0],last_step[1]+directions[last_pos][1])
            if next_step not in path:
                new_paths.append(path + [next_step])
        else:
            for i in ((last_step[0]-1,last_step[1]),(last_step[0]+1,last_step[1]),
                      (last_step[0],last_step[1]-1),(last_step[0],last_step[1]+1)):
                print(i)
                if input_file[i[0]][i[1]] in [".","^",">","<","v"] and i not in path:
                    new_paths.append(path + [i])
    print(new_paths)
    paths = []
    for new_path in new_paths:
        if new_path[-1][0] == len(input_file)-2:
            lengths.append(len(new_path))
        else:
            paths.append(new_path)

print(max(lengths))
    

