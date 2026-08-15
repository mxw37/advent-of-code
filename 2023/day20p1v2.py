input_file = open("day20input.txt","r")
input_file = [i.strip() for i in input_file]

module_type = {}
child_dict = {}
conj_dict = {}
ff_dict = {}

low_pulses = 0
high_pulses = 0

for i in input_file:
    i = i.split(" -> ")
    children = i[1].split(", ")
    if i[0][0] == "%":
        module_name = i[0][1:]
        module_type[module_name] = "ff"
        ff_dict[module_name] = "off"
    elif i[0][0] == "&":
        module_name = i[0][1:]
        module_type[module_name] = "conj"
        conj_dict[module_name] = {}
    else:
        module_name = "broadcaster"
        module_type[module_name] = "broadcaster"
    child_dict[module_name] = children

for i in child_dict.keys():
    for child in child_dict[i]:
        if module_type.get(child) == "conj":
            conj_dict[child][i] = "low"

for i in range(0,1000):
    low_pulses += 1
    pending = [("broadcaster","low")]
    while pending:
        new_pulses = []
        for i in pending:
            for child in child_dict[i[0]]:
                if i[1] == "low":
                    low_pulses += 1
                elif i[1] == "high":
                    high_pulses += 1
                if child not in module_type.keys():
                    pass
                elif module_type[child] == "ff":
                    if i[1] == "low":
                        if ff_dict[child] == "off":
                            ff_dict[child] = "on"
                            new_pulses.append((child,"high"))
                        else:
                            ff_dict[child] = "off"
                            new_pulses.append((child,"low"))
                elif module_type[child] == "conj":
                    conj_dict[child][i[0]] = i[1]
                    if all([j == "high" for j in conj_dict[child].values()]):
                        new_pulses.append((child,"low"))
                    else:
                        new_pulses.append((child,"high"))
        pending = list(new_pulses)

print(high_pulses*low_pulses)


    
