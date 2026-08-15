import numpy as np
from numpy.linalg import inv
from math import modf

input_file = [i.strip() for i in open("day13input.txt","r").readlines()]

total = 0

for i in range(0,len(input_file),4):
    aline = input_file[i].split("Button A: ")[1].split(", ")
    ax = int(aline[0][2:])
    ay = int(aline[1][2:])
    bline = input_file[i+1].split("Button B: ")[1].split(", ")
    bx = int(bline[0][2:])
    by = int(bline[1][2:])
    pline = input_file[i+2].split("Prize: ")[1].split(", ")
    px = int(pline[0][2:])
    py = int(pline[1][2:])
    
    matr1 = np.array([[ax,bx],[ay,by]])
    matr2 = np.array([[px],[py]])

    solution = inv(matr1) @ matr2
    print(solution)

    if solution[0][0]%1 == 0 and solution[1][0]%1 == 0:
        print("VALID")
        total += (3*solution[0][0]+solution[1][0])

print(total)


