input_file = open("day1input.txt","r")
total = 0
def find_num_forward(string):
    nums_dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,
                 "7":7,"8":8,"9":9,"one":1,"two":2,"three":3,"four":4,
                 "five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for i in nums_dict.keys():
        if string.startswith(i):
            return str(nums_dict[i])
    return find_num_forward(string[1:])

def find_num_backward(string,start):
    nums_dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,
                 "7":7,"8":8,"9":9,"one":1,"two":2,"three":3,"four":4,
                 "five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for i in nums_dict.keys():
        if string[-start:].startswith(i):
            return str(nums_dict[i])
    return find_num_backward(string,start+1)
for i in input_file:
    this_val = find_num_forward(i) + find_num_backward(i,1)
    total += int(this_val)
print(total)


