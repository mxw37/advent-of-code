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
    px = int(pline[0][2:])+10000000000000
    py = int(pline[1][2:])+10000000000000
    

    det = (ax*by)-(bx*ay)


    multmatr = [by*px+(-bx)*py,(-ay)*px+ax*py]
    if multmatr[0]%det==0 and multmatr[1]%det==0:
        solution = [multmatr[0]//det,multmatr[1]//det]
        total+=(3*solution[0]+solution[1])

print(total)
