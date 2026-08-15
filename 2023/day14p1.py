input_file = open("day14input.txt","r")

rows = [i.strip() for i in input_file]

columns = ["".join(i) for i in list(zip(*rows))]

new_columns = []

vals = {"O":0,".":1}

for i in columns:
    i = i.split("#")
    for j in range(0,len(i)):
        i[j] = list(i[j])
        i[j].sort(key = lambda char: vals[char])
    new_columns.append("#".join(["".join(k) for k in i]))

new_rows = ["".join(i) for i in list(zip(*new_columns))]

total = 0

for i in range(0,len(new_rows)):
    o_count = new_rows[i].count("O")
    o_count *= (len(new_rows) - i)
    total += o_count

print(total)
