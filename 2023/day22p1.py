input_file = open("day22input.txt","r")
input_file = [i.strip() for i in input_file.readlines()]

bricks_dict = {}
occupied = []
occupied_indexed = []

def can_fall(brick_no,bricks,space):
    for i in bricks[brick_no]:
        below = [i[0],i[1],i[2]-1]
        if below[2] not in space_dict.keys():
            return False
        elif space_dict[below[2]][below[0]][below[1]] not in [".",brick_no]:
            return False
    return True

for ind, brick in enumerate(input_file):
    brick = brick.split("~")
    end1 = eval("["+brick[0]+"]")
    end2 = eval("["+brick[1]+"]")
    bricks_dict[ind] = []
    if end1[0] != end2[0]:
        for i in range(min(end1[0],end2[0]),max(end1[0],end2[0])+1):
            bricks_dict[ind].append([i,end1[1],end1[2]])
    elif end1[1] != end2[1]:
        for i in range(min(end1[1],end2[1]),max(end1[1],end2[1])+1):
            bricks_dict[ind].append([end1[0],i,end1[2]])
    elif end1[2] != end2[2]:
        for i in range(min(end1[2],end2[2]),max(end1[2],end2[2])+1):
            bricks_dict[ind].append([end1[0],end1[1],i])
    else:
        bricks_dict[ind].append(end1)
    for i in bricks_dict[ind]:
        occupied.append(i)
        occupied_indexed.append((i,ind))

space_dict = {}

x_max = max([i[0] for i in occupied])
y_max = max([i[1] for i in occupied])
z_max = max([i[2] for i in occupied])

for z in range(1,z_max+1):
    space_dict[z] = []
    for x in range(0,x_max+1):
        space_dict[z].append([])
        for y in range(0,y_max+1):
            if [x,y,z] in occupied:
                space_dict[z][-1].append(occupied_indexed[occupied.index([x,y,z])][1])
            else:
                space_dict[z][-1].append(".")

for i in range(2,z_max+1):
    
