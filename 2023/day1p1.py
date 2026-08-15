input_file = open("day1input.txt","r")
total = 0
for i in input_file.readlines():
    cal_value = ""
    i = i.strip()
    for j in i:
        if j in "0123456789":
            cal_value += j
            break
    for j in i[::-1]:
        if j in "0123456789":
            cal_value += j
            break
    total += int(cal_value)
print(total)
