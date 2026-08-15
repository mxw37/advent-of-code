input_file = open("day4input.txt","r")
total_score = 0
current_card = 0
total_cards = 0
card_copies = {}
for i in range(1,203): #no. cards is hardcoded here
    card_copies[i] = 1
for i in input_file.readlines():
    current_card += 1
    total_cards += card_copies[current_card]
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
    for i in range(current_card + 1, current_card + 1 + winners):
        card_copies[i] += card_copies[current_card]
print(sum(card_copies.values()))
