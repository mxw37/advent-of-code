import numpy as np

input_file = open("day24input.txt","r")
input_file = [i.strip() for i in input_file.readlines()]

class Hailstone:
    def __init__(self,x,y,z,xv,yv,zv):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.xv = int(xv)
        self.yv = int(yv)
        self.zv = int(zv)

hailstones = []

collisions = 0

for i in input_file:
    i = i.split(" @ ")
    pos = [int(j) for j in i[0].split(", ")]
    vel = [int(j) for j in i[1].split(", ")]
    hailstones.append(Hailstone(pos[0],pos[1],pos[2],vel[0],vel[1],vel[2]))

for i, h1 in enumerate(hailstones):
    for h2 in hailstones[i+1:]:
        A = np.array([[h1.xv,-h2.xv],[h1.yv,-h2.yv]])
        B = np.array([h2.x-h1.x,h2.y-h1.y])
        try:
            C = np.linalg.solve(A,B)
        except:
            C = [-1,-1]
        if (C[0] > 0 and C[1] > 0 and
            200000000000000 < (h1.x + h1.xv*C[0]) < 400000000000000 and
            200000000000000 < (h1.y + h1.yv*C[0]) < 400000000000000):
            collisions += 1

print(collisions)
        
