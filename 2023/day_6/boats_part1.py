import time, sys
start_time = time.time()

def get_min_hold_button(distance_to_beat, remain_time):
    for min_hold_button in range (1, remain_time):
        current_remain_time = remain_time - min_hold_button
        current_distance = current_remain_time*min_hold_button
        if current_distance > distance_to_beat:
            return min_hold_button
    return -1

def get_max_hold_button(distance_to_beat, remain_time):
    for max_hold_button in range (remain_time, 0, -1):
        current_remain_time = remain_time - max_hold_button
        current_distance = current_remain_time*max_hold_button
        
        if current_distance > distance_to_beat:
            return max_hold_button
    return -1

result = 1

file = open("2023/day_6/input.txt")
[times_boat,distances_to_beat] = [list(map(int,line.split(":")[1].split())) for line in file]

if len(times_boat) != len(distances_to_beat) :
    raise Exception("There is a problem with length arrays.. Check your code!")

for index_race in range(len(times_boat)) : 
    distance_to_beat = distances_to_beat[index_race]
    remaining_time = times_boat[index_race]
    
    min_hold = get_min_hold_button(distance_to_beat, remaining_time)
    max_hold = get_max_hold_button(distance_to_beat, remaining_time)
    if min_hold == -1 :
        raise Exception("result -1 min hold")
    if max_hold == -1 :
        raise Exception("result -1 max hold")
    number_ways = max_hold - min_hold + 1
    
    result *= number_ways
print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))