input_file = [i.strip() for i in open("day14input.txt","r").readlines()]

roomx = 101
roomy = 103

midx = (roomx-1)//2
midy = (roomy-1)//2

tl,tr,bl,br = 0,0,0,0

for line in input_file:
    line = line.split(" ")
    line[0] = line[0].split("p=")[1].split(",")
    line[1] = line[1].split("v=")[1].split(",")
    px = int(line[0][0])
    py = int(line[0][1])
    vx = int(line[1][0])
    vy = int(line[1][1])

    endx = (px+100*vx)%roomx
    endy = (py+100*vy)%roomy


    if endx < midx and endy < midy:
        tl += 1
    elif endx < midx and endy > midy:
        bl += 1
    elif endx > midx and endy < midy:
        tr += 1
    elif endx > midx and endy > midy:
        br += 1

print(tr*tl*br*bl)    
