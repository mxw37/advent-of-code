input_file1 = open("day19inputp1.txt","r").readline().strip()
input_file2 = [i.strip() for i in open("day19inputp2.txt","r").readlines()]

input_file1 = [i.strip() for i in input_file1.split(",")]

patterns = {}

for i in input_file1:
    if i[0] not in patterns.keys():
        patterns[i[0]] = [i]
    else:
        patterns[i[0]].append(i)

dp = {}

def check_valid(sequence):
    if sequence == "":
        return True
    result = 0
    for i in patterns.get(sequence[0],[]):
        if sequence.startswith(i):
            if check_valid(sequence[len(i):]):
                valid = True
                break
    dp[sequence] = result
    return result

total = 0

for i in input_file2:
    if check_valid(i):
        total += 1

print(total)
