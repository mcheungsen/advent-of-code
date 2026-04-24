import time
start_time = time.time()

file = open("2023/day_2/input.txt")
loaded_bag = {"blue" : 14, "red" : 12, "green" : 13}

games = [game.strip("\n").split(":")[1].split(";") for game in file]
result = 0
for game_index in range(len(games)):
    current_game = games[game_index]
    game_is_possible = True
    index_set = 0
    while index_set < len(current_game) and game_is_possible is True : 
        current_set = current_game[index_set]
        current_bag = {color : value for value,color in(current_color.split() for current_color in current_set.split(","))}
        for current_color, current_value in current_bag.items():
            if loaded_bag[current_color] < int(current_value):
                game_is_possible = False
                break
        index_set += 1
    if game_is_possible is True :
        result += game_index+1

print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))