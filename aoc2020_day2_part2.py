"""Find the number of valid password according to the condition part 2"""

def find_valid2(password_con):
    # Split condition and password
    condition_pass = password_con.split(" ")
    pass_position = condition_pass[0].split("-")
    first_po = int(pass_position[0]) - 1    # minus 1 because from given condition, first position start at 1
    second_po = int(pass_position[1]) - 1
    char = condition_pass[1][0]
    password = list(condition_pass[2])

    # Check if the password fit the given condition
    if ((password[first_po]==char) & (password[second_po]!=char)) | \
       ((password[first_po]!=char) & (password[second_po]==char)):
        return True
    else:
        return False

# Read input from file
input_file = open("day2_input.txt", "r")
input_list = input_file.read().split("\n")

valid_pass = 0
for p in input_list:
    if find_valid2(p) == True:
        valid_pass += 1
print(valid_pass)