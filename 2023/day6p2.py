import time
def calc_dist(time, press):
    t = time
    p = press
    return p*(t-p)

"""epsilon = 1000000
low= 7078000
high= 40000000
ans = int((high + low)/2)"""


"""while abs(calc_dist(48938595,ans) - 296192812361391) >= epsilon:
    print(abs(calc_dist(48938595,ans) - 296192812361391))
    print(ans)

    ans += 1
    ans = int((high + low)/2)
    time.sleep(0.1)"""
ans = 7075227

while calc_dist(48938595,ans) >= 296192812361391:

    ans += 1



print(ans)
