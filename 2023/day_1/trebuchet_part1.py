import time
start_time = time.time()

file = open("2023/day_1/input.txt")
lines = [line.strip("\n") for line in file]

res = 0

for line in lines :
    index = 0
    first_digit = last_digit = None
    while ((first_digit is None or last_digit is None)
        and index < len(line)) :
        if first_digit is None and line[index].isnumeric() :
            first_digit = line[index]
        if last_digit is None and line[len(line)-1-index].isnumeric()  :
            last_digit = line[len(line)-1-index]
        index += 1
    res += int(first_digit+last_digit)

print(f"the result is = {res}")
print("--- %s seconds ---" % (time.time() - start_time))