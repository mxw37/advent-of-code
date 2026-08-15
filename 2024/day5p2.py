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

incorrect = []

for line in input_file:
    valid = True
    line = [int(j) for j in line.split(",")]
    for i, j in enumerate(line):
        for k in range(i,len(line)):
            if line[k] in rules.get(j,[]):
                valid = False
    if not valid:
        incorrect.append(list(line))

total = 0

for i in incorrect:
    print(i)
    fixed = []
    temp_dict = {}
    for j in i:
        temp_dict[j] = [k for k in rules.get(j,[]) if k in i]
    while i:
        next_page = min(i,key=lambda x: len(temp_dict[x]))
        fixed.append(next_page)
        i.remove(next_page)
        del temp_dict[next_page]
        for j in temp_dict.keys():
            temp_dict[j].remove(next_page)
    total += fixed[int(len(fixed)/2)]
        

print(total)
