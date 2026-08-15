input_file = open("day19p2input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

class ComparisonNode:
    def __init__(self,test_param,operator,threshold,dest):
        self.test_param = test_param
        self.operator = operator
        self.threshold = threshold
        self.dest = dest

class TransferNode:
    def __init__(self,dest):
        self.dest = dest

class AcceptNode:
    def __init__(self):
        pass

class RejectNode:
    def __init__(self):
        pass

import time
start = time.time()
nodes_dict = {}

def get_total(params):
    total = 1
    for i in params.values():
        total *= (i[1]-i[0])
    return total

def DFS(node_key,params):
    #print(params)
    node = nodes_dict[node_key]
    if type(node) == RejectNode:
        return 0
    elif type(node) == AcceptNode:
        return get_total(params)
    elif type(node) == TransferNode:
        return DFS((node.dest,0),params)
    elif type(node) == ComparisonNode:
        true_params = dict(params)
        false_params = dict(params)
        if node.operator == "<":
            if params[node.test_param][1] < node.threshold:
                raise Exception("redundant test detected")
            true_params[node.test_param] = (true_params[node.test_param][0],node.threshold)
            false_params[node.test_param] = (node.threshold,false_params[node.test_param][1])
        else:
            if params[node.test_param][0] > node.threshold:
                raise Exception("redundant test detected")
            true_params[node.test_param] = (node.threshold+1,true_params[node.test_param][1])
            false_params[node.test_param] = (false_params[node.test_param][0],node.threshold+1)
        #print("true params" + str(true_params))
        #print("false params" + str(false_params))
        if node.dest == "A":
            true_total = get_total(true_params)
        elif node.dest == "R":
            true_total = 0
        else:
            true_total = DFS((node.dest,0),true_params)
        false_total = DFS((node_key[0],node_key[1]+1),false_params)
        return (true_total+false_total)
    
for i in input_file:
    workflow_name = i.split("{")[0]
    rules = i.split("{")[1][:-1].split(",")
    for j, rule in enumerate(rules[:-1]):
        nodes_dict[(workflow_name,j)] = ComparisonNode(rule[0],rule[1],int(rule.split(":")[0][2:]),rule.split(":")[1])
    if rules[-1] == "A":
        nodes_dict[(workflow_name,len(rules)-1)] = AcceptNode()
    elif rules[-1] == "R":
        nodes_dict[(workflow_name,len(rules)-1)] = RejectNode()
    else:
        nodes_dict[(workflow_name,len(rules)-1)] = TransferNode(rules[-1])

print(DFS(("in",0),{"x":(1,4001),"m":(1,4001),"a":(1,4001),"s":(1,4001)}))
