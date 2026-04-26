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
    numbers = list(map(int,lines[0].split(":")[1].split()))
    seeds = []
    for i in range (0, len(numbers), 2):
        seeds.append({"seed_source" : numbers[i], "seed_range" : numbers[i+1]})
    
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

for step, operations in steps_list.items():
    seed_index = 0
    while(seed_index < len(seeds)): # TODO ALL SEEDS
        
        # variables to help me with calculations understandings
        seed = seeds[seed_index]
        min_seed = seed["seed_source"]
        max_seed = seed["seed_source"] + seed["seed_range"] - 1
        
        for operation in operations :
            
            # new variables from operation to help me with calculations understandings
            min_operation = operation["source"]
            max_operation = operation["source"] + operation["range"] - 1
            
            if max_seed >= operation["source"] and min_seed <= max_operation :
                # In range ! Now check if we have to divide the seed !
            
                # Division to the left ?
                if min_seed < min_operation :
                    left_seed = {
                        "seed_source" : seed["seed_source"], 
                        "seed_range" : operation["source"]- seed["seed_source"]
                        }
                    
                    in_range_seed = {
                        "seed_source": operation["source"],
                        "seed_range": seed["seed_range"] - left_seed["seed_range"]
                    }
                    
                    seeds.append(left_seed)
                    seed = in_range_seed
                
                # Division to the right ?
                if max_seed > max_operation :
                    in_range_seed = {
                        "seed_source" : seed["seed_source"],
                        "seed_range" : max_operation - seed["seed_source"] + 1
                    }
                    
                    right_seed = {
                        "seed_source" : seed["seed_source"] + in_range_seed["seed_range"],
                        "seed_range" : seed["seed_range"] - in_range_seed["seed_range"]
                    }

                    seeds.append(right_seed)
                    seed = in_range_seed
                    
                # Do the calculation for current_seed now !
                new_source_seed = seed["seed_source"] - operation["source"] + operation["destination"]
                seeds[seed_index] = {"seed_source" : new_source_seed, "seed_range" : seed["seed_range"]}
            
                break
        seed_index +=1


for seed in seeds :
    if min_location > seed["seed_source"] :
        min_location = seed["seed_source"]
        
print(f"The result is = {min_location}")
print("--- %s seconds ---" % (time.time() - start_time))