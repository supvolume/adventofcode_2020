"""Count the number of the question that everyone in the group answer yes"""

# Read input from file
input_file = open("day6_input.txt", "r")
input_list = input_file.read().split("\n\n")

yes_num = 0
for i in input_list:
    passenger = i.split("\n")
    ans_yes = set(list(passenger[0]))
    if len(passenger) > 1:
        for p in passenger[1:]:
            ans_yes = ans_yes & set(list(p))
    yes_num += len(ans_yes)

print(yes_num)