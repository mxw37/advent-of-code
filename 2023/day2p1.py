input_file = open("day2input.txt","r")
ID = 0
possible_sum = 0
for i in input_file:
    possible = True
    ID += 1
    reds = 0
    greens = 0
    blues = 0
    i = i.strip()
    i = i.split(": ")[1]
    i = i.split("; ")
    for j in i:
        j = j.split(", ")
        for k in j:
            if k.endswith(" red") and int(k.split(" ")[0]) > 12:
                possible = False
            if k.endswith(" green") and int(k.split(" ")[0]) > 13:
                possible = False
            if k.endswith(" blue") and int(k.split(" ")[0]) > 14:
                possible = False
    if possible:
        possible_sum += ID
print(possible_sum)
