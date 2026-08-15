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

boxes = {}

for i in input_file:
    if "=" in i:
        label = i.split("=")[0]
        length = int(i.split("=")[1])
        box = HASH(label)
        if box not in boxes.keys():
            boxes[box] = [(label,length)]
        else:
            replaced = False
            for ind, val in enumerate(boxes[box]):
                if val[0] == label:
                    boxes[box][ind] = (label, length)
                    replaced = True
            if not replaced:
                boxes[box].append((label,length))
    elif "-" in i:
        label = i.split("-")[0]
        box = HASH(label)
        if box in boxes.keys():
            for ind, val in enumerate(boxes[box]):
                if val[0] == label:
                    boxes[box].remove(val)

for i in boxes.keys():
    for ind, val in enumerate(boxes[i]):
        total += (i+1)*(ind+1)*(val[1])

print(total)
