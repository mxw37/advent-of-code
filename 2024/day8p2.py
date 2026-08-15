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
                v_coord = antennas[freq][i][0]
                h_coord = antennas[freq][i][1]
                v_shift = antennas[freq][j][0] - v_coord
                h_shift = antennas[freq][j][1] - h_coord
                while 0 <= v_coord <= max_v and 0 <= h_coord <= max_h:
                    antinodes.add((v_coord,h_coord))
                    v_coord += v_shift
                    h_coord += h_shift

print(len(antinodes))
