input_file = [i.strip() for i in open("day4input.txt","r").readlines()]

def xmas_check(cell, direction):
    dir_dict = {"UL":(-1,-1),"U":(-1,0),"UR":(-1,1),
                "L":(0,-1),"R":(0,1),
                "DL":(1,-1),"D":(1,0),"DR":(1,1)}
    dir_tup = dir_dict[direction]
    targets = ["X","M","A","S"]
    try:
        return all([input_file[cell[0]+i*dir_tup[0]][cell[1]+i*dir_tup[1]] == targets[i]
                    for i in range(1,4)])
    except IndexError:
        return False
    """for i in range(1,4):
        print(cell[0]+i*dir_tup[0])
        print(cell[1]+i*dir_tup[1])
        print(input_file[cell[0]+i*dir_tup[0]][cell[1]+i*dir_tup[1]])
        print(input_file[cell[0]+i*dir_tup[0]][cell[1]+i*dir_tup[1]] == targets[i])"""
    
        

directions = ["UL","U","UR","L","R","DL","D","DR"]

##surround grid in O to avoid requiring bounds checking
input_file = ["O" + i + "O" for i in input_file]
input_file.insert(0,"O"*len(input_file[1]))
input_file.append("O"*len(input_file[1]))

xmas_count = 0

for x, i in enumerate(input_file):
    for y, j in enumerate(i):
        if j == "X":
            for d in directions:
                xmas_count += int(xmas_check((x,y),d))

print(xmas_count)
