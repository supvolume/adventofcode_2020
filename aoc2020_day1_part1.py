"""Find the two entries that sum to 2020 and then multiply those two numbers together
https://adventofcode.com/2020/day/1"""

# Read input from file
number_file = open("day1_input.txt", "r")
number_list = number_file.read().split("\n")
number_list = [int(i) for i in number_list]

# Sort the list
number_sort = sorted(number_list)

# Sum the small number with the large number, then move to the next one
small_num = 0
large_num = -1
expect_num = 2020
while True:
    sum_num = number_sort[small_num] + number_sort[large_num]
    if sum_num > expect_num:
        large_num -= 1
    elif sum_num < expect_num:
        small_num += 1
        large_num = -1
    elif sum_num == expect_num:
        break

print("Small number: ", number_sort[small_num])
print("Large number: ", number_sort[large_num])
print("Multiply number: ", number_sort[small_num]*number_sort[large_num])
