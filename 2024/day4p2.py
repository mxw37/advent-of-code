input_file = [i.strip() for i in open("day4input.txt","r").readlines()]

def xmas_check(cell):
    x_cells = [input_file[cell[0]-1][cell[1]-1],
               input_file[cell[0]-1][cell[1]+1],
               input_file[cell[0]+1][cell[1]-1],
               input_file[cell[0]+1][cell[1]+1]]
    return sorted(x_cells) == ["M","M","S","S"] and x_cells[0] != x_cells[3]

##surround grid in O to avoid requiring bounds checking
input_file = ["O" + i + "O" for i in input_file]
input_file.insert(0,"O"*len(input_file[1]))
input_file.append("O"*len(input_file[1]))

xmas_count = 0

for x, i in enumerate(input_file):
    for y, j in enumerate(i):
        if j == "A":
            xmas_count += int(xmas_check((x,y)))

print(xmas_count)
