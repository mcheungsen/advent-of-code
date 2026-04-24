import time
start_time = time.time()


result = 0
file = open("2023/day_3/input_example.txt")
lines = [line for line in file]
def get_indexes_neighbors(index_line:int, index_char: int):
    # TODO : Récup les indexes qui sont des nombres autour du symbole
    pass

def get_neighbors_numbers(index_line:int, index_char: int):
    numbers = get_indexes_neighbors(index_line, index_char)
    # TODO : parcourir les indexes et identifier les nombres
    return numbers

for index_line in range(len(lines)) :
    line = lines[index_line]
    for index_char in range(lines[index_line]) :
        current_char = line[index_char]
        if not current_char.isnumeric() and current_char != ".":
            result += sum(get_neighbors_numbers(index_line, index_char))

print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))