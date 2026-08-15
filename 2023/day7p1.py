from collections import Counter

input_file = open("day7input.txt","r")

bids = {}

for i in input_file.readlines():
    i = i.strip()
    i = i.split(" ")
    bids[i[0]] = int(i[1])

def get_rating(hand):
    """7 = five of a kind
    6 = four of a kind
    5 = full house
    4 = three of a kind
    3 = two pair
    2 = one pair
    1 = high card"""
    cards = ["1","2","3","4","5","6","7","8",
                  "9","T","Q","K","A"]
    if "J" in hand:
        possible = []
        for card in set(hand):
            if card != "J":
                possible.append(get_rating(hand.replace("J",card,1)))
        if hand == "JJJJJ":
            return 7
        return max(possible)
    hand = Counter(hand)
    if 5 in hand.values():
        return 7
    elif 4 in hand.values():
        return 6
    elif 3 in hand.values() and 2 in hand.values():
        return 5
    elif 3 in hand.values():
        return 4
    elif Counter(hand.values()).get(2,0) == 2:
        return 3
    elif Counter(hand.values()).get(2,0) == 1:
        return 2
    elif Counter(hand.values()).get(1,0) == 5:
        return 1

def compare_hands(hand1, hand2):
    """Returns True if hand2 is higher than hand1
    Returns False if hand1 is higher"""
    card_order = ["J","1","2","3","4","5","6","7","8",
                  "9","T","Q","K","A"]
    if get_rating(hand2) > get_rating(hand1):
        return True
    elif get_rating(hand1) > get_rating(hand2):
        return False
    elif get_rating(hand1) == get_rating(hand2):
        for one, two in zip(hand1, hand2):
            if card_order.index(one) < card_order.index(two):
                return True
            elif card_order.index(one) > card_order.index(two):
                return False

hands = list(bids.keys())

n = len(hands)

for i in range(n):
    print(i)
    already_sorted = True
    for j in range(n - i - 1):
        if not compare_hands(hands[j], hands[j+1]):
            hands[j], hands[j+1] = hands[j+1],hands[j]
            already_sorted = False
    if already_sorted:
        break

total = 0

for i in range(0,len(hands)):
    rank = i + 1
    total += rank*bids[hands[i]]

print(total)
