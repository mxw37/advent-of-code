import re

input_file = [i.strip() for i in open("day3input.txt","r").readlines()]

mul_regex = re.compile(r'mul\((?:\d)+,(?:\d)+\)')

total = 0

for line in input_file:
    for i in mul_regex.findall(line):
        i = i[4:-1].split(",")
        total += int(i[0])*int(i[1])

print(total)
