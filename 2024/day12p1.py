import time

input_file = [i.strip() for i in open("day12input.txt","r").readlines()]
input_file = ["_" + i + "_" for i in input_file]
input_file = ["_"*len(input_file[0])] + input_file + ["_"*(len(input_file[0]))]

unvisited = [(i,j) for i in range(1,len(input_file)-1) for j in range(1,len(input_file[0])-1)]

n = 10*len(input_file[0])

"""def calc_cost(group_start):
    group_type = input_file[group_start[0]][group_start[1]]
    members = set()
    new_members = {group_start}
    while new_members:
        next_members = set()
        for m in new_members:
            for n"""

total_cost = 0

def neighbours(i,j):
    return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

while unvisited:
    group_area = 1
    group_perim = 4
    group_start = min(unvisited)
    group_char = input_file[group_start[0]][group_start[1]]
    group = {group_start}
    new_members = {None}
    last_members = {group_start}
    unvisited.remove(group_start)
    while new_members:
        new_members = set()
        for m in last_members:
            for n in neighbours(m[0],m[1]):
                if input_file[n[0]][n[1]] == group_char\
                and (n[0],n[1]) not in group:
                    new_members.add(n)
        for m in new_members:
            try:
                unvisited.remove(m)
            except ValueError:
                pass
            group.add(m)
            group_area += 1
            adj = 0
            for n in neighbours(m[0],m[1]):
                if n in group:
                    adj += 1
            if adj == 1:
                group_perim += 2
            elif adj == 3:
                group_perim -= 2
            elif adj == 4:
                group_perim -= 4
        last_members = new_members
    total_cost += group_area*group_perim

print(total_cost)

    
    
        
