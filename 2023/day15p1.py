input_file = open("day15input.txt","r").readlines()

def HASH(string):
    val = 0
    for i in string:
        val += ord(i)
        val *= 17
        val %= 256
    return val

total = 0

input_file = input_file[0].strip().split(",")

for i in input_file:
    total += HASH(i)

print(total)
