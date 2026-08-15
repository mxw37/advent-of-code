input_file = open("day19workflows.txt","r").readlines()
input_file = [i.strip().strip("}") for i in input_file]

class Workflow:
    def __init__(self,name):
        self.name = name
        self.conditions = []

class Condition:
    pass

#parse_condition function definition

workflows_dict = {}

for i in input_file:
    i = i.split("{")
    workflow_name = i[0]
    new_workflow = Workflow(workflow_name)
    
