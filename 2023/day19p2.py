from operator import mul
from functools import reduce

workflows = [i.strip().strip("{}") for i in open("day19workflows.txt","r").readlines()]

workflows_dict = {}

for i in workflows:
    i = i.split("{")
    workflows_dict[i[0]] = [j.split(":") for j in i[1].split(",")]

def resolve_workflow(workflow, constraints):
    total = 0
    for i in workflows_dict[workflow]:
        #if "<" in i[0] or ">" in i[0] or "=" in i[0]:
        if "<" in i[0]:
            i[0] = i[0].split("<")
            if int(i[0][1]) in range(constraints[i[0][0]][0],constraints[i[0][0]][1]):
                new_constraints = dict(constraints)
                new_constraints[i[0][0]] = [constraints[i[0][0]][0],int(i[0][1])]
                constraints[i[0][0]][0] = int(i[0][1])
                if i[1] == "A":
                    total += reduce(mul,[j[1]-j[0] for j in new_constraints.values()])
                elif i[1] != "R":
                    total += resolve_workflow(workflows_dict[i[1]],new_constraints)
            
        elif i[0] == "A":
            return True
        elif i[0] == "R":
            return False
        else:
            return process_part(part,i[0])

"""test_endpoints = {"x":[1,4001],"m":[1,4001],"a":[1,4001],"s":[1,4001]}
test_ranges = {"x":[],"m":[],"a":[],"s":[]}

total = 0

for i in workflows_dict.values():
    for j in i[:-1]:
        test_endpoints[j[0][0]].append(int(j[0][2:]))

for j in test_endpoints.keys():
    test_endpoints[j] = sorted(test_endpoints[j])
    for ind, endpoint in enumerate(test_endpoints[j][:-1]):
        if ind == 0:
            continue
        if ind == 1:
            test_ranges[j].append((1,endpoint))
        test_ranges[j].append((endpoint,endpoint+1))
        test_ranges[j].append((endpoint+1,test_endpoints[j][ind+1]))

print(len(test_ranges["x"]))
        
for x_range in test_ranges["x"]:
    print("x")
    for m_range in test_ranges["m"]:
        print("m")
        for a_range in test_ranges["a"]:
            print("a")
            for s_range in test_ranges["s"]:
                test_part = {"x":x_range[0],"m":m_range[0],"a":a_range[0],"s":s_range[0]}
                if process_part(test_part,"in"):
                    product = 1
                    for i in [x_range,m_range,a_range,s_range]:
                        product *= (i[1]-i[0])
                    total += product

print(total)"""

