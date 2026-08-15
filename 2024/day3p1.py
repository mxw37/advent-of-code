input_file = [i.strip() for i in open("day3input.txt","r").readlines()]

total = 0

sums = []

import time

for line in input_file:
    line_cp = list(line)
    while line_cp:
       # print(line_cp[:4])
        #time.sleep(0.2)
        if line_cp[:4] == ["m","u","l","("]:
            if ")" in line_cp:
                mul_cand = "".join(line_cp[4:line_cp.index(")")]).split(",")
                #print(mul_cand)
                if len(mul_cand) == 2:
                    try:
                        mul_cand[0] = int(mul_cand[0])
                        mul_cand[1] = int(mul_cand[1])
                        total += (mul_cand[0]*mul_cand[1])
                        sums.append(total)
                        #print("VALID")
                    except ValueError:
                        pass
        line_cp.pop(0)
print(total)
