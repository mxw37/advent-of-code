import time

input_file = open("day9input.txt","r").readline().strip()

blocks = []
files = []
free = []

for i, j in enumerate(input_file):
    blocks.append(int(j))
    if i%2 == 0:
        files.append(int(j))
    elif i%2 == 1:
        free.append(int(j))

blocks_cs = [0]

for i in blocks:
    blocks_cs.append(blocks_cs[-1]+i)

print(blocks)
print(blocks_cs)

checksum = 0

free_pos = 0
files_pos = len(files)-1

for i in range(0,sum(free)):
    if blocks_cs[2*(free_pos+1)]-free[free_pos] > blocks_cs[files_pos*2]:
        break
    files[files_pos] -= 1
    checksum += (blocks_cs[2*(free_pos+1)]-free[free_pos])*files_pos
    if files[files_pos] == 0:
        files_pos -= 1
    free[free_pos] -= 1
    while free[free_pos] == 0:
        free_pos += 1

print(checksum)

print(files)

for i, j in enumerate(files):
    if i%100 == 0:
        print(checksum)
    for k in range(0,j):
        checksum += i*(blocks_cs[i*2]+k)

print(checksum)
