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

file = open("2023/day_6/input.txt")
[remaining_time, distance_to_beat] = [int(line.strip("\n").split(":")[1].replace(" ","")) for line in file]


    
min_hold = get_min_hold_button(distance_to_beat, remaining_time)
max_hold = get_max_hold_button(distance_to_beat, remaining_time)
if min_hold == -1 :
    raise Exception("result -1 min hold")
if max_hold == -1 :
    raise Exception("result -1 max hold")
result = max_hold - min_hold + 1

print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))