input_file = [i.strip() for i in open("day2input.txt","r").readlines()]

safe_reports = 0

def check_safe(i):
    diffs = [i[j] - i[j-1] for j in range(1,len(i))]
    sign = "NA"
    safe = True
    for diff in diffs:
        if diff < -3 or diff > 3 or diff == 0:
            safe = False
            break
        if sign == "NA":
            sign = ("pos" if diff > 0 else "neg")
        elif (sign == "pos" and diff < 0) or (sign == "neg" and diff > 0):
            safe = False
            break
    return safe

for line in input_file:
    line = [int(j) for j in line.split(" ")]
    if check_safe(line):
        safe_reports += 1
        continue
    else:
        for j in range(0,len(line)):
            if check_safe(line[:j] + line[j+1:]):
                safe_reports += 1
                break

print(safe_reports)
