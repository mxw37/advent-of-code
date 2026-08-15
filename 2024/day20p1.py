import time

input_file = [i.strip() for i in open("day20input.txt","r").readlines()]

input_file = ["#" + i + "#" for i in input_file]
input_file.insert(0,"#"*len(input_file[0]))
input_file.append("#"*len(input_file[0]))

def neighbours(pos):
    return ((pos[0]-1,pos[1]),
               (pos[0]+1,pos[1]),
               (pos[0],pos[1]-1),
               (pos[0],pos[1]+1))

def cheat_1(pos):
    return neighbours(pos)

def cheat_2(pos):
    return ((pos[0]-1,pos[1]-1),(pos[0]-1,pos[1]+1),(pos[0]+1,pos[1]-1),
            (pos[0]+1,pos[1]+1),(pos[0]-2,pos[1]),(pos[0]+2,pos[1]),
            (pos[0],pos[1]-2),(pos[0],pos[1]+2))

path = ["X"] #dummy value to avoid breaking path[-2], gets removed later

start_found = False

for i in range(0,len(input_file)):
    for j in range(0,len(input_file[i])):
        if input_file[i][j] == "S":
            path.append((i,j))
            start_found = True
            break
    if start_found:
        break

end_found = False

while not end_found:
    for n in neighbours(path[-1]):
        if input_file[n[0]][n[1]] == "." and n not in path:
            path.append(n)
        elif input_file[n[0]][n[1]] == "E":
            path.append(n)
            end_found = True

print("PATH CONSTRUCTION COMPLETE")

path = path[1:] #remove the dummy value from before

no_cheat_time = len(path)-1

#TEST INPUT VERSION
"""timesave_dict = {}

for i, j in enumerate(path):
    for k in cheat_1(j):
        if input_file[k[0]][k[1]] in [".","E"]:
            cheat_time = len(path)-path.index(k)+i
            timesave = no_cheat_time-cheat_time
            if timesave in timesave_dict.keys():
                timesave_dict[timesave] += 1
            else:
                timesave_dict[timesave] = 1
    for k in cheat_2(j):
        if input_file[k[0]][k[1]] in [".","E"]:
            cheat_time = len(path)-path.index(k)+i+1
            timesave = no_cheat_time-cheat_time
            if timesave in timesave_dict.keys():
                timesave_dict[timesave] += 1
            else:
                timesave_dict[timesave] = 1

print(timesave_dict)"""

#REAL INPUT VERSION

total = 0

for i, j in enumerate(path):
    for k in cheat_1(j):
        if input_file[k[0]][k[1]] in [".","E"]:
            cheat_time = len(path)-path.index(k)+i
            timesave = no_cheat_time-cheat_time
            if timesave >= 100:
                total += 1
    for k in cheat_2(j):
        if input_file[k[0]][k[1]] in [".","E"]:
            cheat_time = len(path)-path.index(k)+i+1
            timesave = no_cheat_time-cheat_time
            if timesave >= 100:
                total += 1

print(total)

