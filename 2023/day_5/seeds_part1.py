import time, sys
start_time = time.time()

def extract_data(file) :
    '''
    get list of seeds, and all steps from seed to location
    return seeds, steps_list
    seeds => list of int
    steps_list => dictionary { step name => List of traductions}
    one traduction => dictionary {destination, start, range}
    '''
    lines = [line.strip("\n") for line in file]
    seeds = list(map(int,lines[0].split(":")[1].split()))
    
    steps_list = {} # key => step name, value => list
    index_line = 2 #0 was for the seeds
    
    while(index_line < len(lines)) :
        step_name = lines[index_line].split()[0]
        index_line+=1
        traductions = []
        while(index_line < len(lines) and lines[index_line] != ""):
            destination, source, traduction_range = list(map(int,lines[index_line].split()))
            current_traduction = {"destination" : destination, "source" : source, "range":traduction_range}
            traductions.append(current_traduction)
            index_line +=1
        steps_list.update({step_name : traductions})
        index_line += 1
    return seeds, steps_list

min_location = sys.maxsize

file = open("2023/day_5/input.txt")
seeds,steps_list = extract_data(file)
print(f"seeds = {seeds}")
print(f"Steps : {steps_list}")

for seed in seeds :
    location = seed
    print(f"current Seed = {seed}")
    print(f"Location start to seed = {location}")
    for key_name, list in steps_list.items():
        print(f"Step = {key_name}")
        for current_dict in list:
            if (location >= current_dict["source"] 
            and location < (current_dict["source"] + current_dict["range"]) ):
                location = location + current_dict["destination"] - current_dict["source"]
                print(f"in range = f{current_dict}")
                print(f"location changed = {location}")
                print()
                break
    if location < min_location :
        min_location = location
        print("------new MIN-------")
    print("-----")

print(f"The result is = {min_location}")
print("--- %s seconds ---" % (time.time() - start_time))