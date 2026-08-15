input_file = open("day17input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

options_dict ={("N",False):["N","E","W"],
               ("E",False):["N","S","E"],
               ("S",False):["S","E","W"],
               ("W",False):["N","S","W"],
               ("N",True):["E","W"],
               ("E",True):["N","S"],
               ("S",True):["E","W"],
               ("W",True):["N","S"]}
direct_dict = {"N":(-1,0),"E":(0,1),"S":(1,0),"W":(0,-1)}

grid = {}

for r, i in enumerate(input_file):
    for c, j in enumerate(i):
        grid[(r,c)] = int(j)
