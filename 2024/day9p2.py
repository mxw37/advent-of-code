input_file = open("day9input.txt","r").readline().strip()

blocks = []
files = []
free = []
free_sizes = {i:[] for i in range(0,10)}

for i, j in enumerate(input_file):
    blocks.append(int(j))
    if i%2 == 0:
        files.append(int(j))
    elif i%2 == 1:
        free.append(int(j))
        for k in range(0,int(j)+1):
            free_sizes[k].append(i)

blocks_cs = [0]

for i in blocks:
    blocks_cs.append(blocks_cs[-1]+i)

checksum = 0


##CHANGE FREE_SIZES TO USE INDICES FROM BLOCKS_CS
print(free_sizes)
for i in range(len(files)-1,-1,-1):
    print(i)
    if free_sizes[files[i]]:
        if free_sizes[files[i]][0] < i*2:
            dest = free_sizes[files[i]][0]
            print("DEST = " + str(dest))
            for j in range(0,files[i]):
                checksum += (blocks_cs[+j)*i
            for j in range(free[(dest-1)//2]-files[i]+1,free[(dest-1)//2]):
                free_sizes[j].remove(dest)
            for j in range(free[(dest-1)//2]-files[i]+1):
                free_sizes[j][free_sizes[j].index(dest)] = dest+files[i]
            free[(dest-1)//2] -= files[i]
            files[i] = 0
            print(free_sizes)


for i, j in enumerate(files):
    if i%100 == 0:
        print(checksum)
    for k in range(0,j):
        checksum += i*(blocks_cs[i*2]+k)

print(checksum)
