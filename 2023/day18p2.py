import time

input_file = open("day18input.txt","r")

def split_consecutive(lst):
    sublists = [[lst[0]]]
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1] + 1:
            sublists[-1].append(lst[i])
        else:
            sublists.append([lst[i]])
    return sublists

def check_dead_end(dug,endpoint1,endpoint2):
    if (endpoint1[0]-1,endpoint1[1]) in dug and (endpoint2[0]-1,endpoint2[1]) in dug:
        return True
    if (endpoint1[0]+1,endpoint1[1]) in dug and (endpoint2[0]+1,endpoint2[1]) in dug:
        return True
    return False

dug = {(0,0)}
current = (0,0)
directions = {"0":(0,1),"1":(-1,0),"2":(0,-1),"3":(1,0)}
input_file = input_file.readlines()

for i in input_file:
    print(i)
    hexstr = i.split(" ")[2]
    distance = int(hexstr[2:7],16)
    direction = directions[hexstr[7]]
    for j in range(distance):
        current = (direction[0]+current[0],direction[1]+current[1])
        dug.add(current)

dug_rows = set([i[0] for i in dug])

volume = 0

for row in range(min(dug_rows),max(dug_rows)+1):
  #  print(row)
    dug_cols = sorted(list(set([i[1] for i in dug if i[0] == row])))
    dug_cols = split_consecutive(dug_cols)
    channel_edges = [[None,None]]
    for i in dug_cols:
       # print(i)
        if len(i) == 1 or  check_dead_end(dug,(row,i[0]),(row,i[-1])) == False:
            if len(channel_edges[-1]) == 2:
                channel_edges.append([i[0]])
            else:
                channel_edges[-1].append(i[-1])
        elif len(channel_edges[-1]) == 2 or len(channel_edges) == 1:
            volume += (i[-1] - i[0] + 1)
  #  print(channel_edges)
    for i in channel_edges[1:]:
        volume += (i[1] - i[0] + 1)
    #volume += (max(dug_cols) - min(dug_cols) + 1)
  #  print(volume)
