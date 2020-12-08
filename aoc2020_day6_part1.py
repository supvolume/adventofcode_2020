"""Count the number of answer yes (the unique character) for each group of passenger
https://adventofcode.com/2020/day/6"""

# Read input from file
input_file = open("day6_input.txt", "r")
input_list = input_file.read().split("\n\n")

sum_yes = 0
for i in input_list:
    sum_yes += len(set(i)-set("\n"))

print(sum_yes)