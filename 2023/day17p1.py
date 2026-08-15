input_file = open("day17input.txt","r")

class Path:
    def __init__(self, cells):
        self.cells = cells
        self.turns = []
        self.heat_loss = 0

    def add_cell(self, cell, heat_loss_val):
        self.cells.append(cell)
        self.heat_loss += heat_loss_val
    
input_file = [i.strip() for i in input_file.readlines()]
input_file = [[int(j) for j in i] for i in input_file]

paths = [[(None,(0,0))]]


