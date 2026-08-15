input_file = open("day4input.txt","r")
total_score = 0
current_card = 0
for i in input_file.readlines():
    current_card += 1
    i = i.strip()
    i = i.split(": ")[1]
    winning = i.split(" | ")[0]
    actual = i.split(" | ")[1]
    winning = [int(j.strip()) for j in winning.split(" ") if j != ""]
    actual = [int(j.strip()) for j in actual.split(" ") if j != ""]
    winners = 0
    for i in actual:
        if i in winning:
            winners += 1
    if winners > 0:
        total_score += (2**(winners - 1))
print(total_score)
