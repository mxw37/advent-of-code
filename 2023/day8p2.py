#Rank 381
instructions = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"
input_file = open("day8input.txt","r")
nodes = {}
for i in input_file:
    i = i.strip()
    i = i.split(" = ")
    nodes[i[0]] = (i[1][1:4],i[1][-4:-1])
def find_steps(start):
    current = start
    count = -1
    steps = 0
    while True:
        count += 1
        steps += 1
        if count == len(instructions):
            count = 0
        if instructions[count] == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        if current[-1] == "Z":
            return steps
for i in ['AAA','BFA','DFA','XFA','QJA','SBA']:
    print(find_steps(i))
#After this I took the LCM of all find_steps values, this was done manually via command line
