input_file = open("day12input.txt","r")

def starsandbars(items, bins, current_poss):
    if current_poss == []:
        unplaced = items - bins + 2
        distribution = [[0] + [1]*(bins-2) + [0]]
        if unplaced == 0:
            return [tuple(distribution[0])]
        else:
            return starsandbars(unplaced,bins,distribution)
    else:
        possibilities = []
        for i in range(0,len(current_poss)):
            for j in range(0,bins):
                cp_copy = list(current_poss[i])
                cp_copy[j] += 1
                possibilities.append(cp_copy)
        if items == 1:
            return set([tuple(i) for i in possibilities])
        else:
            return starsandbars(items - 1, bins, possibilities)

def conv_to_row(op, damg):
    return_str = ""
    for i in range(0,len(damg)):
        return_str += ("."*op[i])
        return_str += ("#"*damg[i])
    return_str += "."*op[-1]
    return return_str

def check_consistency(unknown, option):
    consistent = True
    for i, j in zip(unknown, option):
        if i == j or i == "?":
            pass
        else:
            consistent = False
    return consistent

total = 0

for i in input_file.readlines():
    possible = 0
    i = i.strip()
    i = i.split(" ")
    length = len(i[0])
    damaged = eval("[" + i[1] + "]")
    options = starsandbars(length - sum(damaged),len(damaged)+1,[])
    for j in options:
        j_conv = conv_to_row(j, damaged)
        if check_consistency(i[0], j_conv):
            possible += 1
    total += possible

print(total)

