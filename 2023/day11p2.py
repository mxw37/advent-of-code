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

def get_empty_rows(row1,row2):
    empty_rows_count = 0
    for i in range(min(row1,row2),max(row1,row2)):
        if i in empty_rows:
            empty_rows_count += 1
    return empty_rows_count

def get_empty_cols(col1, col2):
    empty_cols_count = 0
    for i in range(min(col1,col2),max(col1,col2)):
        if i in empty_cols:
            empty_cols_count += 1
    return empty_cols_count

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


galaxy_locs = []

for row in range(0,len(grid)):
    for col in range(0,len(grid[row])):
        if grid[row][col] == "#":
            galaxy_locs.append((row,col))

dist_sum = 0

for i in range(0,len(galaxy_locs)):
    for j in range(i+1,len(galaxy_locs)):
        one = galaxy_locs[i]
        two = galaxy_locs[j]
        dist_sum += abs(two[0]-one[0])
        dist_sum += abs(two[1]-one[1])
        dist_sum += 999999*get_empty_rows(one[0],two[0])
        dist_sum += 999999*get_empty_cols(one[1],two[1])

print(dist_sum)
