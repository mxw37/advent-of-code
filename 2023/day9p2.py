input_file = open("day9input.txt","r")

def get_last(lst):
    if len(set(lst)) == 1:
        return lst[0]
    else:
        diffs = [lst[i+1]-lst[i] for i in range(0,len(lst)-1)]
        return lst[0] - get_last(diffs)

total = 0

for i in input_file:
    i = i.strip()
    i = i.split(" ")
    i = [int(j) for j in i]
    total += get_last(i)

print(total)
