input_file = [i.strip() for i in open("day1input.txt","r").readlines()]

input_file = [i.split() for i in input_file]

first_list = sorted([int(i[0]) for i in input_file])
second_list = sorted([int(i[1]) for i in input_file])

print(sum([abs(first_list[i]-second_list[i]) for i in range(0,len(first_list))]))
