import math
import time

start = time.time()

input_file = [i.strip() for i in open("day7input.txt","r")]

def check_valid(nums,target):
    if len(nums) == 2:
        return nums[0] + nums[1] == target or \
               nums[0] * nums[1] == target or \
               (10**(len(str(nums[1]))))*nums[0] + nums[1] == target
    elif math.prod(nums) == target:
        return True
    else:
        return check_valid([nums[0]+nums[1]] + nums[2:],target) or \
               check_valid([nums[0]*nums[1]] + nums[2:],target) or \
               check_valid([(10**(len(str(nums[1]))))*nums[0] + nums[1]]+nums[2:],
                           target)
        
total = 0

for ind, line in enumerate(input_file):
    #print(line)
    if ind % 10 == 0:
        print(ind)
    line = line.split(": ")
    line[0] = int(line[0])
    line[1] = [int(i) for i in line[1].split(" ")]
    if check_valid(line[1],line[0]):
        #print("VALID")
        total += line[0]

print(time.time()-start)

print(total)
