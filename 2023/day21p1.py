input_file = [i.strip() for i in open("day21input.txt","r").readlines()]

#surround the edge with rocks to avoid requiring special case handling for borders
input_file = ["#"+i+"#" for i in input_file]
input_file = ["#"*len(input_file[0])] + input_file + ["#"*len(input_file[0])]

def get_options(grid, coords):
    options = []
    row = coords[0]
    col = coords[1]
    for i in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
        if grid[i[0]][i[1]] == ".":
            options.append(i)
    return options

memo = {}

for i in range(len(input_file)):
    for j in range(len(input_file[i])):
        if input_file[i][j] == "S":
            start_row = i
            start_col = j

paths = {((start_row,start_col),6)}
new_paths = {None}
ends = set()

while new_paths:
    print(len(new_paths))
    new_paths = set()
    for i in paths:
        if i[1] == 0:
            ends.add(i[0])
        elif i[0] in memo:
            for j in memo[i[0]]:
                new_paths.add((j,i[1]-1))
        else:
            options = get_options(input_file,i[0])
            memo[i[0]] = options
            for j in options:
                new_paths.add((j,i[1]-1))
    paths = set(new_paths)

#KNOWN BUG - THIS PROGRAM FINDS ALL ENDINGS EXCEPT FOR THE START POINT. CAUSE UNKNOWN

print(len(ends))
