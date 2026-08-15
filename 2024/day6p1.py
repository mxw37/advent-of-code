input_file = [i.strip() for i in open("day6input.txt","r")]

obstacles = []
grid_dict = {}

for i in range(0,len(input_file)):
    for j in range(0,len(input_file[i])):
        if input_file[i][j] == "^":
            guard_pos = (i,j)
            grid_dict[(i,j)] = "."
        else:
            grid_dict[(i,j)] = input_file[i][j]

guard_dir = "U"
dir_dict = {"U":(-1,0),"R":(0,1),"D":(1,0),"L":(0,-1)}
turn_dict = {"U":"R","R":"D","D":"L","L":"U"}

visited = {guard_pos}

while True:
    dest = (guard_pos[0]+dir_dict[guard_dir][0],guard_pos[1]+dir_dict[guard_dir][1])
    front = grid_dict.get(dest,"X")
    if front == "X":
        print(len(visited))
        break
    elif front == "#":
        guard_dir = turn_dict[guard_dir]
    elif front == ".":
        guard_pos = dest
        visited.add(dest)

