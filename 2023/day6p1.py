def calc_dist(time, press):
    t = time
    p = press
    return p*(t-p)

ways = []

for time, dist in [[48,296],[93,1928],[85,1236],[95,1391]]:
    possible_dists = []
    for press_opt in range(0,time):
        possible_dists.append(calc_dist(time,press_opt))
    ways.append(len([i for i in possible_dists if i > dist]))

print(ways)
