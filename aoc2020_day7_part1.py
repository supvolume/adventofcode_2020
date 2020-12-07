"""Count the number of bag colors that can eventually contain at least one shiny gold bag"""

import re


def find_bag(condition):
    contain_bag = {}
    condition_gr = re.search(r'(.*bags?)(?:\scontain\s)(.*)(?:\.)', condition)
    if condition_gr.group(2) == "no other bag":
        return condition_gr.group(1), contain_bag
    else:
        bags = condition_gr.group(2).split(", ")
        for i in bags:
            contain_bag[i[2:]] = i[0]
    return condition_gr.group(1), contain_bag


def check_shiny(all_bag, bag_name):
    if "shiny gold bag" in all_bag[bag_name]:
        return True
    else:
        return False


# Read input from file
input_file = open("day7_input.txt", "r")
# Convert bags into singular form
input_list = input_file.read().replace("bags", "bag").split("\n")

# Create dict of each bag, identify which bag and the amount of the bag it can contain
all_bag = {}
for i in input_list:
    main_bag, sub_bag = find_bag(i)
    all_bag[main_bag] = sub_bag
"""
# ===Part 1===
# Keep adding the bag that relate to shiny gold bag
# Loop until there is no change in the unique bag list
bag_list = []
bag_list_len = 0
while True:
    for k, v in all_bag.items():
        if check_shiny(all_bag, k):
            bag_list.append(k)
        elif len(v) != 0:
            for i in v:
                if i in bag_list:
                    bag_list.append(k)
    if bag_list_len == len(set(bag_list)):
        break
    else:
        bag_list_len = len(set(bag_list))
print(len(set(bag_list)))
"""

# ===Part 2=== (not finish)

def count_bag(bag_name, all_bag):
    bag_num = 0
    for k, v in all_bag[bag_name].items():
        bag_num += int(v)
    return bag_num, list(all_bag[bag_name].keys())

tot_bag_num = 0
check_list = ["shiny gold bag"]
while len(check_list) > 0:
    n, add_bag = count_bag(check_list[0], all_bag)
    tot_bag_num += n
    check_list += add_bag
    print(check_list, n)
    check_list.pop(0)
print(tot_bag_num)