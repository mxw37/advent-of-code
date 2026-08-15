input_file = open("day3input.txt","r")

input_file = [i.strip() for i in input_file.readlines()]

#surround grid in . to avoid requiring special case handling for edge units
input_file = ["."+i+"." for i in input_file]
input_file = [["."]*len(input_file[0])] + input_file + [["."]*len(input_file[0])]

def get_parts(grid):
    part_locs = []
    part_active = False
    for i in range(0,len(grid)):
        part_active = False
        for j in range(0,len(grid[i])):
            if grid[i][j] in "1234567890":
                if part_active:
                    part_locs[-1].append((i,j))
                else:
                    part_locs.append([(i,j)])
                    part_active = True
            else:
                if part_active:
                    part_active = False
    return part_locs

def get_adj(part, grid):
    """takes coordinates of a part as input
    returns locations of any * symbols adjacent to that part
    assumes that part locations are in ascending order"""
    possible = []
    stars = []
    if len(part) == 1:
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if part == [(8, 99)]:
                    print((part[0][0]+i,part[0][1]+j))
                possible.append((part[0][0]+i,part[0][1]+j))
                if part == [(8,99)]:
                    print(possible)

        possible.remove((part[0][0],part[0][1]))
    elif len(part) == 2:
        #r and c stand for row and column respectively
        r1 = part[0][0]
        c1 = part[0][1]
        r2 = part[1][0]
        c2 = part[1][1]
        possible = [(r1-1,c1-1),(r1-1,c1),(r1,c1-1),
                    (r1+1,c1-1),(r1+1,c1),(r2-1,c2),
                    (r2-1,c2+1),(r2,c2+1),(r2+1,c2),
                    (r2+1,c2+1)]
    else:
        #r and c stand for row and column respectively
        #f and L stand for first and last respectively
        #L is capitalised to distinguish it from numeral 1
        rf = part[0][0]
        cf = part[0][1]
        RL = part[-1][0]
        CL = part[-1][1]
        possible = [(rf-1,cf-1),(rf-1,cf),(rf,cf-1),
                    (rf+1,cf-1),(rf+1,cf)]
        for i in part[1:-1]:
            possible.append((i[0]-1,i[1]))
            possible.append((i[0]+1,i[1]))
        possible.extend([(RL-1,CL),
                    (RL-1,CL+1),(RL,CL+1),(RL+1,CL),
                    (RL+1,CL+1)])
    
    for i in possible:
        if grid[i[0]][i[1]] == "*":
            stars.append(i)

    """commented out return statement is only for testing"""
    #return possible
    if (7,99) in stars:
        print(part)
        print(stars)
    return stars

def get_part_num(part, grid):
    """assumes part indices are in order"""
    part_str = ""
    for i in part:
        part_str += grid[i[0]][i[1]]
    return int(part_str)

parts = get_parts(input_file)

star_locs = []

for i in parts:
    star_locs.extend(get_adj(i,input_file))

parts_dict = {}
parts_dict_rev = {}

for ind, part in enumerate(parts):
    parts_dict[ind] = part
    for j in part:
        parts_dict_rev[j] = ind

gears = set()

for i in star_locs:
    if star_locs.count(i) == 2:
        gears.add(i)

total = 0

for i in gears:
    adj_parts = set()
    for j in [-1,0,1]:
        for k in [-1,0,1]:
            if (i[0]+j,i[1]+k) in parts_dict_rev.keys():
                adj_parts.add(tuple(parts_dict[parts_dict_rev[(i[0]+j,i[1]+k)]]))
    adj_parts = list(adj_parts)
    total += (get_part_num(adj_parts[0],input_file)*get_part_num(adj_parts[1],input_file))

print(total)
