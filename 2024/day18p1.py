import time

input_file = [i.strip() for i in open("day18input.txt","r").readlines()]

obstacles = []

for i in input_file[:1024]:
    i = i.split(",")
    obstacles.append((int(i[0]),int(i[1])))

min_x = 0
min_y = 0
max_x = 70
max_y = 70

visited = set()

positions = {(0,0)}

steps = 0

def neighbours(pos):
    options = ((pos[0]-1,pos[1]),
               (pos[0]+1,pos[1]),
               (pos[0],pos[1]-1),
               (pos[0],pos[1]+1))
    return (i for i in options if min_x <= i[0] <= max_x and min_y <= i[1] <= max_y)

while (max_x,max_y) not in positions:
    new_positions = set()
    for p in positions:
        for n in neighbours(p):
            if n not in obstacles and n not in visited:
                new_positions.add(n)
    visited = visited.union(positions)
    positions = set(new_positions)
    steps += 1


print(steps)

