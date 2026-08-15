input_file = [i.strip() for i in open("day1input.txt","r").readlines()]

input_file = [i.split() for i in input_file]

list1 = []
list2dict = {}

for i in input_file:
    list1.append(int(i[0]))
    if int(i[1]) in list2dict.keys():
        list2dict[int(i[1])] += 1
    else:
        list2dict[int(i[1])] = 1

simil_sum = 0

for i in list1:
    simil_sum += i*(list2dict.get(i,0))

print(simil_sum)
