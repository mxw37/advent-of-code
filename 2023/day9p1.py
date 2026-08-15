input_file = open("day9input.txt","r")

def get_next(lst):
    if len(set(lst)) == 1:
        return lst[0]
    else:
        diffs = [lst[i+1]-lst[i] for i in range(0,len(lst)-1)]
        return lst[-1] + get_next(diffs)

total = 0

for i in input_file:
    i = i.strip()
    i = i.split(" ")
    i = [int(j) for j in i]
    total += get_next(i)

print(total)
