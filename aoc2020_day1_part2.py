"""Find the three entries that sum to 2020 and then multiply those three numbers together"""

# Read input from file
number_file = open("day1_input.txt", "r")
number_list = number_file.read().split("\n")
number_list = [int(i) for i in number_list]

# Sort the list
number_sort = sorted(number_list)

# Brute force way
expect_num = 2020

for i in range(len(number_sort)):
    for j in range(len(number_sort)):
        for k in range(len(number_sort)):
            if number_sort[i] + number_sort[j] + number_sort[k] == expect_num:
                print("First number: " + str(number_sort[i]) + "\n" \
                    + "Second number: "+ str(number_sort[j]) + "\n" \
                    + "Third number: " + str(number_sort[k]) + "\n" \
                    + "Multiply number: " + str(number_sort[i]*number_sort[j]*number_sort[k]) + "\n" )
                break
