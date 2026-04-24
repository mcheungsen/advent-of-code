import time, math
start_time = time.time()

file = open("2023/day_2/input.txt")
games = [game.strip("\n").split(":")[1].split(";") for game in file]
result = 0

for game_index in range(len(games)):
    current_game = games[game_index]
    minimal_bag = {"red":0,"green":0,"blue":0}
    for current_set in current_game:
        current_bag = {color : int(value) for value,color in(current_color.split() for current_color in current_set.split(","))}
        for current_color, current_value in current_bag.items():
            if minimal_bag[current_color] < current_value:
                minimal_bag[current_color] = current_value
    power  = math.prod(minimal_bag.values())
    result += power
print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))