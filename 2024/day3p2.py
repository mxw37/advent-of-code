import re

input_file = "".join([i.strip() for i in open("day3input.txt","r").readlines()])

input_file = input_file.split("don't()")

mul_regex = re.compile(r'mul\((?:\d)+,(?:\d)+\)')

input_file[0] = [input_file[0]]

for i in range(1,len(input_file)):
    input_file[i] = input_file[i].split("do()")[1:]

def process_line(line):
    total = 0
    for i in mul_regex.findall(line):
        i = i[4:-1].split(",")
        total += int(i[0])*int(i[1])
    return total

print(sum([process_line(j) for i in input_file for j in i]))

