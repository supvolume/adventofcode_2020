"""Find the number of valid password according to the condition"""

def find_valid(password_con):
    # Split condition and password
    condition_pass = password_con.split(" ")
    pass_limit = condition_pass[0].split("-")
    lower_limit = int(pass_limit[0])
    upper_limit = int(pass_limit[1])
    char = condition_pass[1][0]
    password = list(condition_pass[2])

    # Count the number of character in password
    char_num = password.count(char)

    # Check if it within the limit or not
    if (char_num >= lower_limit) & (char_num <= upper_limit):
        return True
    else:
        return False

# Read input from file
input_file = open("day2_input.txt", "r")
input_list = input_file.read().split("\n")

valid_pass = 0
for p in input_list:
    if find_valid(p) == True:
        valid_pass += 1
print(valid_pass)