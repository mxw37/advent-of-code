input_file = open("day22input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

space_dict = {}
bricks_dict = {}
lines = []
for k, i in enumerate(input_file):
    i = [eval("(" + j + ")") for j in i.split("~")]
    lines.append(i)
    if i[0] == i[1]:
        units = [i[0]]
    elif i[0][0] != i[1][0]:
        units = [(j,i[0][1],i[0][2]) for j in range(i[0][0],i[1][0]+1)]
    elif i[0][1] != i[1][1]:
        units = [(i[0][0],j,i[0][2]) for j in range(i[0][1],i[1][1]+1)]
    elif i[0][2] != i[1][2]:
        units = [(i[0][0],i[0][1],j) for j in range(i[0][2],i[1][2]+1)]
    for unit in units:
        space_dict[unit] = k
    bricks_dict[k] = units

def can_fall(brick):
    return (0 not in [i[2] for i in bricks_dict[brick]]) and \
            all([space_dict.get((i[0],i[1],i[2]-1),None) in [None,brick] for i in bricks_dict[brick]])

def do_fall(brick):
    #print(brick)
    for i in bricks_dict[brick]:
        del space_dict[i]
        space_dict[(i[0],i[1],i[2]-1)] = brick
    bricks_dict[brick] = [(i[0],i[1],i[2]-1) for i in bricks_dict[brick]]

brick_fell = True
while brick_fell:
    brick_fell = False
    for brick in range(0,len(input_file)):
        if can_fall(brick):
            do_fall(brick)
            brick_fell = True

print("ALL BRICKS FALLEN")

v_supports_k = {i: set() for i in range(0,len(input_file))}
k_supports_v = {i: set() for i in range(0,len(input_file))}

for brick in range(0,len(input_file)):
    if 0 not in [i[2] for i in bricks_dict[brick]]:
        supporters = []
        for j in bricks_dict[brick]:
            below = space_dict.get(((j[0],j[1],j[2]-1)),None)
            if below not in [brick,None]:
                supporters.append(below)
        v_supports_k[brick] = supporters
        for s in supporters:
            k_supports_v[s].add(brick)
        

def disintegrate(brick,fallen):
    for i in k_supports_v[brick]:
        if all([j == brick or j in fallen for j in v_supports_k[i]]):
            fallen.add(i)
            fallen = fallen.union(disintegrate(i,fallen))
    return fallen

total = 0

for brick in range(0,len(input_file)):
    total += len(disintegrate(brick,set()))
print(total)


