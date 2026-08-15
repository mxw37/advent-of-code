#Rank 738
instructions = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"
input_file = open("day8input.txt","r")
nodes = {}
for i in input_file:
    i = i.strip()
    i = i.split(" = ")
    nodes[i[0]] = (i[1][1:4],i[1][-4:-1])
count = -1
steps = 0
current = "AAA"
while True:
    count += 1
    steps += 1
    if count == len(instructions):
        count = 0
    if instructions[count] == "L":
        current = nodes[current][0]
    else:
        current = nodes[current][1]
    if current == "ZZZ":
        break
print(steps)
