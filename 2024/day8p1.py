input_file = [i.strip() for i in open("day8input.txt","r").readlines()]

max_v = len(input_file)-1
max_h = len(input_file[0])-1

antinodes = set()

antennas = {}

for i, line in enumerate(input_file):
    for j, k in enumerate(line):
        if k != ".":
            try:
                antennas[k].append((i,j))
            except:
                antennas[k] = [(i,j)]

for freq in antennas.keys():
    for i in range(0,len(antennas[freq])):
        for j in range(0,len(antennas[freq])):
            if i != j:
                cand = (2*antennas[freq][i][0]-antennas[freq][j][0]
                         ,2*antennas[freq][i][1]-antennas[freq][j][1])
                if 0 <= cand[0] <= max_v and 0 <= cand[1] <= max_h:
                    antinodes.add(cand)

print(len(antinodes))
