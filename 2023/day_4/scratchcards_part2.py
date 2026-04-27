import time, math
start_time = time.time()

result = 0

file = open("2023/day_4/input.txt")
lines = [line.strip("\n") for line in file]
copies = [1 for _ in range(len(lines))]


for index_line in range(len(lines)) :
    line = lines[index_line]
    [winning_cards, my_cards] = [list(map(int,numbers.split())) for numbers in line.split(":")[1].split("|")]
    matches = 0
    for winning_card in winning_cards :
        index_card = 0
        while index_card < len(my_cards) :
            if winning_card == my_cards[index_card]:
                matches += 1
                copies[index_line+matches] += 1*copies[index_line]
                break
            index_card += 1

result = sum(copies)
print(f"The result is = {result}")
print("--- %s seconds ---" % (time.time() - start_time))