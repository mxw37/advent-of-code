input_file = [int(i) for i in open("day11input.txt","r").readline().strip().split(" ")]

dp = {}

def num_stones(stone,blinks):
    if (stone,blinks) in dp.keys():
        return dp[(stone,blinks)]
    elif blinks == 0:
        return_val = 1
    elif stone == 0:
        return_val = num_stones(1,blinks-1)
    elif len(str(stone))%2 == 0:
        return_val = num_stones(int(str(stone)[:int(len(str(stone))/2)]),blinks-1) \
               +num_stones(int(str(stone)[int(len(str(stone))/2):]),blinks-1)
    else:
        return_val = num_stones(stone*2024,blinks-1)
    dp[(stone,blinks)] = return_val
    return return_val

total = 0

for i in input_file:
    #print(i)
    total += num_stones(i,25)

print(total)
