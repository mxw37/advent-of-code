input_file = [i.strip() for i in open("day6input.txt","r")]

obstacles = []
og_grid = {}

for i in range(0,len(input_file)):
    for j in range(0,len(input_file[i])):
        if input_file[i][j] == "^":
            guard_start = (i,j)
            og_grid[(i,j)] = "."
        else:
            og_grid[(i,j)] = input_file[i][j]

def process_input(grid):
    """Takes grid as input.
        Returns 1 if guard gets stuck in loop,
        -1 if guard goes off edge"""
    guard_pos = guard_start
    guard_dir = "U"
    dir_dict = {"U":(-1,0),"R":(0,1),"D":(1,0),"L":(0,-1)}
    turn_dict = {"U":"R","R":"D","D":"L","L":"U"}

    states = {(guard_pos,"U")}

    while True:
        dest = (guard_pos[0]+dir_dict[guard_dir][0],guard_pos[1]+dir_dict[guard_dir][1])
        front = grid.get(dest,"X")
        #print(front)
        if front == "X":
            return -1
        elif front == "#":
            guard_dir = turn_dict[guard_dir]
        elif front == ".":
            guard_pos = dest
        if (guard_pos,guard_dir) in states:
            return 1
        else:
            states.add((dest,guard_dir))

options = {(i,j) for i in range(0,len(input_file)) for j in range(0,len(input_file[0]))
           if (i,j) not in obstacles and (i,j) != guard_start}

count = 0

print(len(options))

for i, o in enumerate(options):
    if i%1000  == 0:
        print(i)
    #print(o)
    if process_input(og_grid | {o:"#"}) == 1:
        count += 1

print(count)
