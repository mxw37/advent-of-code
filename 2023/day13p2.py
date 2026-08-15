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

def differ_by_one(list1,list2):
    differences = 0
    differ_location = 0
    for i in range(0,len(list1)):
        if list1[i] != list2[i]:
            differences += 1
            differ_location = i
    return (differences == 1, differ_location)

def check_dbo(grid,line): #dbo stands for differ by one
    '''line is the index of the row above the reflection line or the column to the left of it'''
    side1 = []
    side2 = []
    for i, j in zip(range(line,-1,-1),range(line+1,len(grid))):
        side1.append(grid[i])
        side2.append(grid[j])
    if not differ_by_one(side1,side2)[0]:
        return False
    else:
        differ_item = differ_by_one(side1,side2)[1]
      #  print(side1)
        if differ_by_one(list(side1[differ_item]),list(side2[differ_item]))[0]:
            return True
        else:
            return False


input_file = split(input_file,'')

total = 0

for i in input_file:
    rows = list(i)
    columns = []
    #for k in rows:
       # print("".join(k))
    for j in range(0,len(rows[0])):
        columns.append([k[j] for k in rows])
    for row in range(0,len(rows)-1):
        if check_dbo(rows,row):
            total += ((row+1)*100)
          #  print(total)
            break
    for col in range(0,len(columns)-1):
        if check_dbo(columns,col):
            total += (col+1)
         #   print(total)
            break

print(total)

    
