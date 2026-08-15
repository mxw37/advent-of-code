import itertools
import time

start = time.time()

input_file = [i.strip() for i in open("day7input.txt","r")]

def eval_ops(nums,ops):
    if len(nums) == 2:
        return eval(str(nums[0]) + ops[0] + str(nums[1]))
    else:
        return eval_ops([eval(str(nums[0]) + ops[0] + str(nums[1]))] + nums[2:],ops[1:])

total = 0

for ind, line in enumerate(input_file):
    #if ind % 10 == 0:
     #   print(ind)
    valid = False
    line = line.split(": ")
    line[0] = int(line[0])
    line[1] = line[1].split(" ")
    for i in list(itertools.product(["+","*"],repeat=len(line[1]))):
        eval_result = eval_ops(line[1],i)
        if eval_result == line[0]:
            valid = True
            break
    if valid:
        total += line[0]
    
print(time.time()-start)

print(total)
