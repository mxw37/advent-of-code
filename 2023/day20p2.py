input_file = open("day20input.txt","r")
input_file = [i.strip() for i in input_file.readlines()]

module_types = {}

"""dictionary of str -> list where the value is a list of the strings
that transmit to that module"""
sources = {}

"""dictionary of str -> int where the value of each module is the interval
in button presses between every two low pulses it receives"""
reception_cycle = {}

"""dictionary of str -> int where the value of each module is the interval
in button presses between every two low pulses it sends"""
transmission_cycle = {}

for i in input_file:
    i = i.split(" -> ")
    source = i[0]
    dests = i[1].split(", ")
    if i[0][0] == "%":
        i[0] = i[0][1:]
        module_types[i[0]] = "ff"
    elif i[0][0] == "&":
        i[0] = i[0][1:]
        module_types[i[0]] = "conj"
    else:
        module_types[i[0]] = "broadcaster"
    modules.append(i[0])
    for dest in dests:
        try:
            sources[dest].append(source)
        except KeyError:
            sources[dest] = [source]

unresolved = list(modules)
unresolved.remove("broadcaster")

reception_cycle["broadcaster"] = 1
transmission_cycle["broadcaster"] = 1

while 
