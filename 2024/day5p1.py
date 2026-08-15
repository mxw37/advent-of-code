input_file = [i.strip() for i in open("day5input.txt","r")]

#dict of int -> [int] where value represents the pages that must be
#printed before key
rules = {}

while True:
    line = input_file.pop(0).split("|")
    if line == [""]:
        break
    try:
        rules[int(line[1])].append(int(line[0]))
    except KeyError:
        rules[int(line[1])] = [int(line[0])]

total = 0

for line in input_file:
    valid = True
    line = [int(j) for j in line.split(",")]
    for i, j in enumerate(line):
        for k in range(i,len(line)):
            if line[k] in rules.get(j,[]):
                valid = False
    if valid:
        total += line[int(len(line)/2)]

print(total)
