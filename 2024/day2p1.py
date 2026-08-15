input_file = [i.strip() for i in open("day2input.txt","r").readlines()]

safe_reports = 0

for i in input_file:
    i = [int(j) for j in i.split(" ")]
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
    print(safe)
    safe_reports += int(safe)
    
print(safe_reports)
