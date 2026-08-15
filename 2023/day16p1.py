input_file = open("day16input.txt","r")

def get_next_loc(grid, location, direction):
   # print(location)
  #  print(direction)
    if direction == "up":
        new_loc = (location[0]-1,location[1])
    elif direction == "down":
        new_loc = (location[0]+1,location[1])
    elif direction == "right":
        new_loc = (location[0],location[1]+1)
    elif direction == "left":
        new_loc = (location[0],location[1]-1)
    new_tile = grid[new_loc[0]][new_loc[1]]
    fs_map = {"up":"right","down":"left","left":"down","right":"up"}
    bs_map = {"up":"left","down":"right","left":"up","right":"down"}
    if new_tile == ".":
        return ((new_loc, direction),)
    elif new_tile == "|" and direction in ["up","down"]:
        return ((new_loc, direction),)
    elif new_tile == "-" and direction in ["left","right"]:
        return ((new_loc, direction),)
    elif new_tile == "|" and direction in ["left","right"]:
        return ((new_loc,"up"),(new_loc,"down"))
    elif new_tile == "-" and direction in ["up","down"]:
        return ((new_loc,"left"),(new_loc,"right"))    
    elif new_tile == "/":
        return ((new_loc,fs_map[direction]),)
    elif new_tile == "\\":
        return ((new_loc,bs_map[direction]),)
    elif new_tile == "E":
        return None

input_file = [i.strip() for i in input_file.readlines()]
input_file = ["E" + i + "E" for i in input_file]
input_file = ["E"*len(input_file[0])] + input_file + ["E"*len(input_file[0])]
    
energised = [(1,1)]
paths = [((1,1),"down")]
memo = [((1,1),"down")]

while True:
    new_paths = []
    for path in paths:
        new_path = get_next_loc(input_file, path[0],path[1])
        if new_path != None:
            for i in new_path:
                #print(new_path)
                new_paths.append(i)
    energised.extend([i[0] for i in new_paths])
  #  print(all([i in memo for i in new_paths]))
    if all([i in memo for i in new_paths]):
        print("END")
        break
 #   print(len(memo))
 #   print(memo)
 #   print(new_paths)
    paths = [i for i in new_paths if i not in memo]
    memo.extend([i for i in new_paths if i not in memo])
    #print(new_paths)
    
print(len(set(energised)))
    
