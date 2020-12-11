"""Simulate your seating area by applying the seating rules repeatedly until no seats change state.
Count the number of seats end up occupied
https://adventofcode.com/2020/day/11"""


# Return the list of neighbor seat
def check_neighbor(seat_col, seat_row, all_seat):
    neighbor_seat = []
    for i in range(seat_col-1, seat_col+2):
        for j in range(seat_row-1, seat_row+2):
            if 0 <= i < len(all_seat) and 0 <= j < len(all_seat[0]) and (i != seat_col or j != seat_row):
                neighbor_seat.append(all_seat[i][j])
    return neighbor_seat


# Read input from file
input_file = open("day11_input.txt", "r")
input_list = input_file.read().split("\n")
seat_map = input_list.copy()


# Check each seat
while True:
    for col in range(len(input_list)):
        for row in range(len(input_list[0])):
            neighbor = check_neighbor(col, row, input_list)
            occupied = neighbor.count("#")
            if input_list[col][row] == "L" and occupied == 0:
                if row == len(input_list)-1:
                    seat_map[col] = seat_map[col][:row]+"#"
                else:
                    seat_map[col] = seat_map[col][:row] + "#" + seat_map[col][row+1:]
            elif input_list[col][row] == "#" and occupied >= 4:
                if row == len(input_list)-1:
                    seat_map[col] = seat_map[col][:row]+"L"
                else:
                    seat_map[col] = seat_map[col][:row] + "L" + seat_map[col][row+1:]
    if seat_map != input_list:
        input_list = seat_map.copy()
    else:
        break

count_occ = 0
for row in seat_map:
    count_occ += row.count("#")
print(count_occ)