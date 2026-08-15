input_file = open("day12input.txt","r")
input_file = [i.strip() for i in input_file.readlines]
input_file = [i.split(" ") for i in input_file]
input_file = [[5*i[0],5*i[1]] for i in input_file]

for record in input_file:
    springs = record[0]
    damaged = record[1]

    """keys are 2-tuples where the first element is a list of all damaged
    spring locations so far and the second element is a boolean value representing
    whether the last spring was damaged"""
    options = {}

    if springs[0] == ".":
        options = {([],False):1}
    elif springs[0] == "#":
        options = {([1],True):1}
    elif springs[0] == "#":
        options = {([],False):1,([1],True):1}

    for spring in springs[1:]:
        if spring == ".":
            
