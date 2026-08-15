workflows = [i.strip().strip("{}") for i in open("day19workflows.txt","r").readlines()]
parts = [i.strip().strip("{}") for i in open("day19parts.txt","r").readlines()]

workflows_dict = {}

for i in workflows:
    i = i.split("{")
    workflows_dict[i[0]] = [j.split(":") for j in i[1].split(",")]

def process_part(part,workflow):
    x = part["x"]
    m = part["m"]
    a = part["a"]
    s = part["s"]
    for i in workflows_dict[workflow]:
        if "<" in i[0] or ">" in i[0] or "=" in i[0]:
            if eval(i[0]):
                if i[1] == "A":
                    return True
                elif i[1] == "R":
                    return False
                else:
                    return process_part(part,i[1])
        elif i[0] == "A":
            return True
        elif i[0] == "R":
            return False
        else:
            return process_part(part,i[0])

total = 0

for i in parts:
    part_dict = {}
    i = [j.split("=") for j in i.split(",")]
    part_dict["x"] = int(i[0][1])
    part_dict["m"] = int(i[1][1])
    part_dict["a"] = int(i[2][1])
    part_dict["s"] = int(i[3][1])
    if process_part(part_dict,"in"):
        total += sum(part_dict.values())
    
