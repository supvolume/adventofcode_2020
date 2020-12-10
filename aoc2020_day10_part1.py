"""Find the number of differences of 1 jolt and number of differences of 3 jolts
https://adventofcode.com/2020/day/10
"""

# Read input from file
input_file = open("day10_input.txt", "r")
input_list = input_file.read().split("\n")
input_list = sorted([int(i) for i in input_list])

one_dif = 1
three_dif = 1
for i in range(len(input_list)-1):
    if input_list[i+1] - input_list[i] == 1:
        one_dif += 1
    elif input_list[i+1] - input_list[i] == 3:
        three_dif += 1


print(one_dif * three_dif)
