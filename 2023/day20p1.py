input_file = open("day20input.txt","r").readlines()
input_file = [i.strip() for i in input_file]

modules_dict = {}

def Module:
    def __init__(self,name,destinations):
        self.name = name
        self.pulse_status = "low"
        self.destinations = destinations

def FlipFlopModule(Module):
    def resolve_pulse(self, pulse_type, origin):
        if pulse_type == "high":
            if self.pulse_status = "low":
                self.pulse_status = "high"
            else:
                self.pulse_status = "low"

def ConjunctionModule(Module):
    def __init__(self,name,destinations):
        self.name = name
        self.pulse_status = "low"
        self.destinations = destinations
        self.input_dict = {}
        
    def resolve_pulse(self, pulse_type, origin):
        
