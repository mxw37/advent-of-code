input_file = open("day13input.txt","r").readlines()

input_file = [i.strip() for i in input_file]

def split(sequence, sep):
    chunk = []
    ret_list = []
    for val in sequence:
        if val == sep:
            ret_list.append(chunk)
            chunk = []
        else:
            chunk.append(val)
    ret_list.append(chunk)
    return ret_list

def check_sym(grid,line):
    '''line is the index of the row above the reflection line or the column to the left of it'''
    pairs_list = []
    for i, j in zip(range(line,-1,-1),range(line+1,len(grid))):
        pairs_list.append((i,j))
    return all([grid[i[0]] == grid[i[1]] for i in pairs_list])


input_file = split(input_file,'')

total = 0

for i in input_file:
    rows = list(i)
    columns = []
    for k in rows:
        print("".join(k))
    for j in range(0,len(rows[0])):
        columns.append([k[j] for k in rows])
    for row in range(0,len(rows)-1):
        if check_sym(rows,row):
            total += ((row+1)*100)
            print(total)
            break
    for col in range(0,len(columns)-1):
        if check_sym(columns,col):
            total += (col+1)
            print(total)
            break

print(total)

    
