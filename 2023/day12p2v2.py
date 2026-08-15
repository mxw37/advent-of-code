"""Debug log:
Accidentally wrote input_file instead of i[0] at one point
Originally my program returned 1 arrangement for everything.
Noticed that the program was never going into the spring == "?" branch and
spent a while figuring out how until I noticed that I had accidentally
pasted the wrong version of the input into the input file.
"""

input_file = open("day12input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

cum_total = 0

part_2 = True

for row in input_file:
    row = row.split(" ")
    if part_2:
        springs = "?".join(5*[row[0]])
        damaged = 5*eval("(" + row[1] + ")")
    else:
        springs = row[0]
        damaged = eval("(" + row[1] + ")")
    """dict of tuple -> int
    1st element of key is the list of damaged spring locations up to that point
    2nd element of key is the last character
    int is the number of options with that combination"""
    memo = {((),"."):1}
    for ind, spring in enumerate(springs):
        #print(spring)
        new_memo = {}
        for i in memo.keys():
            new_keys = []
            if spring == ".":
                if i[1] == "#":
                    if i[0][-1] == damaged[len(i[0])-1]:
                        new_keys = [(i[0],"."),]
                else:
                    new_keys = [i]
            elif spring == "#":
                if i[1] == ".":
                    if len(i[0]) < len(damaged):
                        new_keys = [(i[0]+(1,),"#")]
                else:
                    if i[0][-1] < damaged[len(i[0])-1]:
                        new_keys = [(i[0][:-1] + (i[0][-1]+1,),"#")]
            elif spring == "?":
                if ind == 0:
                    new_keys = [((1,),"#"),((),".")]
                else:
                    if i[1] == ".":
                        new_keys.append(i)
                        if len(i[0]) < len(damaged):
                            new_keys.append((i[0]+(1,),"#"))
                    else:
                        if i[0][-1] == damaged[len(i[0])-1]:
                            new_keys = [(i[0],"."),]
                        if i[0][-1] < damaged[len(i[0])-1]:
                            new_keys = [(i[0][:-1] + (i[0][-1]+1,),"#")]
            #print(new_keys)
            for new_key in new_keys:
                if new_key in new_memo.keys():
                    new_memo[new_key] += memo[i]
                else:
                    new_memo[new_key] = memo[i]
        memo = dict(new_memo)
        #print(memo)
        #print("\n")
    options = 0
    for i in memo.keys():
        if i[0] == damaged:
            options += memo[i]
    cum_total += options
    #print(options)
    #print("_________________________________________________")
print(cum_total)
