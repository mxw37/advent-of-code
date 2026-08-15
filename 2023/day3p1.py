input_file = open("day3input.txt","r")
rows = []
parts = []
for i in input_file.readlines():
    i = i.strip()
    rows.append(list(i))
rows = [["."] + i + ["."] for i in rows]

#surround the grid with . to avoid needing special case handling for edge units
rows.insert(0,["."]*len(rows[0]))
rows.append(["."]*len(rows[0]))

def is_part(row, column):
    global rows
    if rows[row][column] == "." or rows[row][column] in "1234567890":
        return False
    else:
        return True
    
def check_adj(row, column):
    global rows
    return_val = False
    for i in [row-1,row,row+1]:
        for j in [column-1,column,column+1]:
            if is_part(i,j):
                return_val = True
    return return_val

#parsing of parts
part_active = False
for row in range(1,len(rows)-1):
    for col in range(1,len(rows[1])-1):
        if rows[row][col] in "1234567890":
            if part_active:
                parts[-1].append((row,col))
            else:
                parts.append([(row,col)])
                part_active = True
        else:
            if part_active:
                part_active = False

parts_sum = 0

#identification of adjacency
for part in parts:
    is_eng_part = False
    for part_of_part in part:
        try:
            if check_adj(part_of_part[0],part_of_part[1]):
                is_eng_part = True
                break
        except:
            print(part_of_part)
            raise Exception("EAFAESFAESFEASFAESF")
    if is_eng_part:
        part_str = ""
        for part_of_part in part:
            part_str += rows[part_of_part[0]][part_of_part[1]]
     #   print(part_str)
        parts_sum += int(part_str)

print(parts_sum)
