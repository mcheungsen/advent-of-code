import time
start_time = time.time()

numbers = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

def get_digit_number(line:str, index:int):
    if line[index].isnumeric() :
        return line[index]
    for string_number, value_number in numbers.items():
        for i in range(len(string_number)):
            if index + i < len(line) : 
                if string_number[i] != line[index+i]:
                    break
                elif i == len(string_number)-1 :
                    return value_number
    return None

file = open("2023/day_1/input.txt")
lines = [line.strip("\n") for line in file]

result = 0

for line in lines :
    first_digit = last_digit = None
    index = 0
    while ((first_digit is None or last_digit is None)
        and index < len(line)) :
        if first_digit is None :
            first_digit = get_digit_number(line, index)
        if last_digit is None : 
            last_digit = get_digit_number(line, len(line)-1-index)
        index += 1
    if first_digit is None or last_digit is None :
        raise Exception(f"There is a problem in my code. I need to fix this : first digit is = {first_digit}, last Digit is = {last_digit}")
    result+=int(first_digit+last_digit)

print(f"the result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))