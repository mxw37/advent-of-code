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

def manhattan(pos1,pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

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

#TEST INPUT VERSION
"""timesave_dict = {}
for i in range(0,len(path)):
    for j in range(i+50,len(path)):
        timesave = (j-i)-manhattan(path[i],path[j])
        if timesave >= 50:
            if timesave in timesave_dict.keys():
                timesave_dict[timesave] += 1
            else:
                timesave_dict[timesave] = 1"""

total = 0
for i in range(0,len(path)):
    if i%50 == 0:
        print(i)
    for j in range(i+50,len(path)):
        timesave = (j-i)-manhattan(path[i],path[j])
        if timesave >= 100 and manhattan(path[i],path[j]) <= 20:
            total += 1

