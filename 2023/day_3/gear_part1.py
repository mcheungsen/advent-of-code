import time
start_time = time.time()


result = 0
file = open("2023/day_3/input_example.txt")
lines = [line for line in file]

def get_indexes_neighbors(index_line:int, index_char: int):
    neighbors_indexes = []
    
    for i_line in range(-1,2):
        for j_char in range(-1,2):
            current_line = index_line + i_line
            current_char = index_char + j_char
            # in range ?
            if (current_line >= 0 and current_line<len(lines)
                and current_char >= 0 and current_char<len(lines[current_line])):
                # Number ?
                if lines[index_line+i_line][index_char+j_char].isnumeric():
                    neighbors_indexes.append((current_line, current_char))
    return neighbors_indexes

def get_neighbors_numbers(index_line:int, index_char: int):
    indexes_numbers = get_indexes_neighbors(index_line, index_char)
    numbers = []
    
    while(len(indexes_numbers) > 0):
        index_line = indexes_numbers[0][0]
        index_char = indexes_numbers[0][1]
        
        line = lines[index_line]
        # step 1 : first index from this index line
        while ((index_char-1 >= 0 ) # in range 
        and (line[index_char-1].isnumeric())) :
            index_char -= 1
            
        # step 2 : get the whole number and check if in indexes list -> remove when used
        res = ""
        while(index_char < len(line) # in range 
        and line[index_char].isnumeric()): 
            res += line[index_char]
            current_tuple = (index_line, index_char)
            if current_tuple in indexes_numbers :
                indexes_numbers.remove(current_tuple)
            index_char += 1
        numbers.append(int(res))
    return numbers

for index_line in range(len(lines)) :
    line = lines[index_line]
    for index_char in range(len(lines[index_line])) :
        current_char = line[index_char]
        if not current_char.isnumeric() and current_char != ".":
            result += sum(get_neighbors_numbers(index_line, index_char))

print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))