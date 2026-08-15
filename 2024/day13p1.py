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

    cx = 0
    cy = 0

    possible = False

    min_tokens = 500

    while cx <= px and cy <= py:
        b_req = (px-cx)/bx
        if int(b_req) == b_req:
            if (py-cy)/by == b_req:
                possible = True
                min_tokens = min(min_tokens,3*(cx/ax)+b_req)
        cx += ax
        cy += ay

    if possible == True:
        total += min_tokens

print(total)

