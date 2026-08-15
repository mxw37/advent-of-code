input_file = open("day2input.txt","r")
ID = 0
power_sum = 0
for i in input_file:
    ID += 1
    reds = []
    greens = []
    blues = []
    i = i.strip()
    i = i.split(": ")[1]
    i = i.split("; ")
    for j in i:
        j = j.split(", ")
        for k in j:
            if k.endswith(" red"):
                reds.append(int(k.split(" ")[0]))
            if k.endswith(" green"):
                greens.append(int(k.split(" ")[0]))
            if k.endswith(" blue"):
                blues.append(int(k.split(" ")[0]))
    power_sum += (max(reds))*(max(greens))*(max(blues))
print(power_sum)
