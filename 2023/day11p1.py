input_file = open("day11input.txt","r")

grid = []

for i in input_file:
    i = i.strip()
    i = list(i)
    grid.append(i)

def add_column(lst, index):
    for i in range(0,len(lst)):
        lst[i].insert(index,".")
    return lst

def get_column(lst,col_num):
    return [i[col_num] for i in lst]

empty_rows = []
empty_cols = []

for i in range(0,len(grid)):
    if all([j == "." for j in grid[i]]):
        empty_rows.append(i)

for i in range(0,len(grid[0])):
    if all([j == "." for j in get_column(grid,i)]):
        empty_cols.append(i)

empty_rows.reverse()
empty_cols.reverse()

empty_row = ["."]*len(grid[0])

for i in empty_rows:
    grid.insert(i,["."]*len(grid[0]))

for i in empty_cols:
    grid = add_column(grid,i)

galaxy_locs = []

for row in range(0,len(grid)):
    for col in range(0,len(grid[row])):
        if grid[row][col] == "#":
            galaxy_locs.append((row,col))

dist_sum = 0

for i in galaxy_locs:
    for j in galaxy_locs:
        if i != j:
            dist_sum += abs(j[0]-i[0])
            dist_sum += abs(j[1]-i[1])

print(dist_sum/2)
