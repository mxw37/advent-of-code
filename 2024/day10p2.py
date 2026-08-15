input_file = [i.strip() for i in open("day10input.txt","r").readlines()]

if_dict = {}

for i in range(0,len(input_file)):
    for j in range(0,len(input_file[i])):
        if_dict[(i,j)] = int(input_file[i][j])

def neighbours(coords):
    return ((coords[0]-1,coords[1]),
            (coords[0]+1,coords[1]),
            (coords[0],coords[1]-1),
            (coords[0],coords[1]+1))

def get_score(trailhead):
    positions = [trailhead]
    for i in range(1,10):
        new_positions = []
        for p in positions:
            for n in neighbours(p):
                if if_dict.get(n,-1) == i:
                    new_positions.append(n)
        positions = list(new_positions)
    return len(positions)

total = 0

for k in if_dict.keys():
    if if_dict[k] == 0:
        total += get_score(k)

print(total)
