input_file = open("day14input.txt","r")

rows = [i.strip() for i in input_file]

cols = ["".join(i) for i in list(zip(*rows))]

def tilt_ns(rows, direction):
    new_columns = []
    columns = ["".join(i) for i in list(zip(*rows))]
    if direction == "north":
        vals = {"O":0,".":1}
    else:
        vals = {"O":1,".":0}
    for i in columns:
        i = i.split("#")
        for j in range(0,len(i)):
            i[j] = list(i[j])
            i[j].sort(key = lambda char: vals[char])
        new_columns.append("#".join(["".join(k) for k in i]))
    new_rows = ["".join(i) for i in list(zip(*new_columns))]
    return new_rows

def tilt_ew(rows, direction):
    new_rows = []
    if direction == "west":
        vals = {"O":0,".":1}
    else:
        vals = {"O":1,".":0}
    for i in rows:
        i = i.split("#")
        for j in range(0,len(i)):
            i[j] = list(i[j])
            i[j].sort(key = lambda char: vals[char])
        new_rows.append("#".join(["".join(k) for k in i]))
    return new_rows

def cycle(rows):
    rows = tilt_ns(rows,"north")
    rows = tilt_ew(rows,"west")
    rows = tilt_ns(rows,"south")
    rows = tilt_ew(rows,"east")
    return rows

def get_load(rows):
    load = 0
    for i in range(0,len(rows)):
        o_count = rows[i].count("O")
        o_count *= (len(rows)-i)
        load += o_count
    return load

archive = [rows]
cycles_done = 0

while True:
    rows = cycle(rows)
    cycles_done += 1
    if rows in archive:
        print("REPEAT!")
        print(cycles_done)
        print(archive.index(rows))
        break
    archive.append(rows)

"""This code only goes up to the part where we find the first repeat.
The part where I simulate the remaining cycles was done manually via the command line"""
