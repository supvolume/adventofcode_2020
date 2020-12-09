"""Find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it
https://adventofcode.com/2020/day/9"""


# Find the sum of two number in the list that meet the expected value
def find_valid_sum(num_list, expected_value):
    start_index = 0
    while start_index < len(num_list):
        for i in num_list[start_index+1:]:
            if int(num_list[start_index]) + int(i) == int(expected_value):
                return True
        start_index += 1
    return False


# Read input from file
input_file = open("day9_input.txt", "r")
input_list = input_file.read().split("\n")

# ===Part 1===
# Check the list of number to find number that did not meet the condition
# The number of member in the checking list is the same
invalid_num = ""
start_list = 0
end_list = 25  # change to the number of length of preamble
for i in range(len(input_list)-end_list):
    num_list = input_list[start_list:end_list]
    valid_sta = find_valid_sum(num_list, input_list[end_list])
    if valid_sta == False:
        invalid_num = input_list[end_list]
    start_list += 1
    end_list += 1
print("part 1 answer: ", invalid_num)


# ===Part 2===
start_list2 = 0
found = False
sum_continuous = []
while start_list2 < len(input_list) and found == False:
    for i in range(start_list2, len(input_list)):
        sum_continuous.append(int(input_list[i]))
        if sum(sum_continuous) == int(invalid_num):
            #print(sum_continuous)
            print("part 2 answer: ", min(sum_continuous)+max(sum_continuous))
            found = True
        elif sum(sum_continuous) > int(invalid_num):
            sum_continuous = []
            break
    start_list2 += 1