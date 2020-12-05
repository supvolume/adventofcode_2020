"""Count the number of tree (#) when starting at the top-left corner of the map and following a slope"""


def count_hash(x_increase, y_increase):
    # Count the number of "#"
    hash_num = 0
    x_coor = x_increase
    y_coor = y_increase

    while x_coor <= len(input_list) - 1:
        if input_list[x_coor][y_coor] == "#":
            hash_num += 1
        x_coor += x_increase
        y_coor = ((y_coor + y_increase) % len(input_list[0]))
    return hash_num


# ===Part 1===
# Read input from file
input_file = open("day3_input.txt", "r")
input_list = input_file.read().split("\n")

# Slope in part 1 is right 3 and down 1
print("Answer of part 1: ", count_hash(1,3))

# ===Part 2===
print("Answer of part 2: ", count_hash(1,1)*count_hash(1,3)*count_hash(1,5)*count_hash(1,7)*count_hash(2,1))

