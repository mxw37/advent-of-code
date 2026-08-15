input_file = [int(i) for i in open("day11input.txt","r").readline().strip().split(" ")]

total = 0

for i in input_file:
    stones = [i]
    for j in range(0,25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone))%2 == 0:
                new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
                new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
            else:
                new_stones.append(stone*2024)
        stones = list(new_stones)
    total += len(stones)

print(total)
