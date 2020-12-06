"""Find seat row from binary partitioning"""


def find_row(row_code,min_row, max_row):
    if len(row_code) == 0:
        return min_row
    else:
        if row_code[0] =="F":
            max_row = int((max_row-min_row)/2) + min_row
        else:
            min_row = int((max_row-min_row)/2) + min_row + 1
        #print(row_code[0]+", "+str(min_row)+", "+ str(max_row))
        return find_row(row_code[1:], min_row, max_row)


def find_col(col_code,min_col, max_col):
    if len(col_code) == 0:
        return min_col
    else:
        if col_code[0] =="L":
            max_col = int((max_col-min_col)/2) + min_col
        else:
            min_col = int((max_col-min_col)/2) + min_col + 1
        #print(col_code[0]+", "+str(min_col)+", "+ str(max_col))
        return find_col(col_code[1:], min_col, max_col)


# Read input from file
input_file = open("day5_input.txt", "r")
input_list = input_file.read().split("\n")

# ===Part 1===
# Find maximum seat number
max_num = 0
for code in input_list:
    row_num = find_row(code[:7], 0, 127)
    col_num = find_col(code[7:], 0, 7)
    seat_num = row_num * 8 + col_num
    if seat_num > max_num:
        max_num = seat_num
print(max_num)

# ===Part 2===
all_seat = []
for code in input_list:
    row_num = find_row(code[:7], 0, 127)
    col_num = find_col(code[7:], 0, 7)
    seat_num = row_num * 8 + col_num
    all_seat.append(seat_num)

seat_range = set(range(min(all_seat), max(all_seat)+1))

# Find the number that not in the min and max range, which is empty seat
print(set(all_seat) ^ seat_range)