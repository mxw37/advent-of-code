from copy import deepcopy
import time

input_file = open("day17input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes

class Transition:
    def __init__(self,direction):
        self.direction = direction

class Path:

    options_dict ={"N":["N","E","W"],"E":["N","S","E"],"S":["S","E","W"],
                   "W":["N","S","W"]}
    must_turn_dict = {"N":["E","W"],"E":["N","S"],"S":["E","W"],
                      "W":["N","S"]}
    transitions_dict = {"N":(-1,0),"E":(0,1),"S":(1,0),"W":(0,-1)}
    
    def __init__(self,graph,start):
        self.graph = graph
        self.start = start
        self.heat_loss = 0
        self.current = start
        self.transitions = []

    def get_options(self):
        if not self.transitions:
            #assumes that the crucible starts in the top left corner
            return ["E","S"]
        last_3 = [i.direction for i in self.transitions[-3:]]
        if len(set(last_3)) == 1:
            return self.must_turn_dict[last_3[-1]]
        else:
            return self.options_dict[last_3[-1]]

    def check_transition(self,new_transition):
        direct_tuple = Path.transitions_dict[new_transition.direction]
        new_current = (self.current[0]+direct_tuple[0],
                        self.current[1]+direct_tuple[1])
        return (new_current in self.graph.nodes.keys())

    def add_transition(self,new_transition):
        self.transitions.append(new_transition)
        direct_tuple = Path.transitions_dict[new_transition.direction]
        self.current = (self.current[0]+direct_tuple[0],
                        self.current[1]+direct_tuple[1])
        self.heat_loss += self.graph.nodes[self.current]

grid = {}

for r, i in enumerate(input_file):
    for c, j in enumerate(i):
        grid[(r,c)] = int(j)

grid = Graph(grid)

pq = {i:float("inf") for i in grid.nodes.keys()}
pq = {(0,0)}
visited = []

shortest_dist = {(0,0):0}
shortest_path = {(0,0):Path(grid,(0,0))}

counter = 0

while pq:
    loopstart = time.time()
    current_node = min(pq,key=lambda x:shortest_dist[x])
    current_path = shortest_path[current_node]
    pq.remove(current_node)
    if current_node in visited:
        continue
    visited.append(current_node)
    for i in current_path.get_options():
        new_path = deepcopy(current_path)
        if new_path.check_transition(Transition(i)):
            new_path.add_transition(Transition(i))
            if new_path.current not in shortest_dist.keys() or new_path.heat_loss < shortest_dist[new_path.current]:
                shortest_dist[new_path.current] = new_path.heat_loss
                shortest_path[new_path.current] = new_path
                pq.add(new_path.current)

        
