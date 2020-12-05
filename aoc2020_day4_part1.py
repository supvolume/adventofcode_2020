"""Count the number of valid passports - those that have all required fields. Treat cid as optional."""

import re


# Verify that the field is exist
def find_field(passport):
    valid_pass = ("byr:" in passport) * ("iyr:" in passport) * ("eyr:" in passport) \
                * ("hgt:" in passport) * ("hcl:" in passport) * ("ecl:" in passport) \
                * ("pid:" in passport)
    return valid_pass


# Verify the value in the field with regex
def field_with_con(passport):
    # Match birth year
    #birth_y = int(re.search(r'(?:byr:)(\d+)', passport).group(1))
    #if (birth_y < 1920) | (birth_y > 2002):
     #   return 0

    # Match issue year
    #issue_y = int(re.search(r'(?:iyr:)(\d+)', passport).group(1))
    #if (issue_y < 2010) | (issue_y > 2020):
    #    return 0

    # Match expiration year
    #exp_y = int(re.search(r'(?:eyr:)(\d+)', passport).group(1))
    #if (exp_y == None) | (exp_y < 2020) | (exp_y > 2030):
     #   return 0

    # Match height
    height = re.search(r'(?:hgt:)(\d+)(cm|in)', passport)
    print(height)
    if height == None:
        print(height)
        return 0
    elif height.group(2) == None:
        print("no unit")
        return 0
    elif (height.group(2) == "cm") & ((int(height.group(1)) < 150) | (int(height.group(1)) > 193)):
        print(height)
        return 0
    elif (height.group(2) == "in") & ((int(height.group(1)) < 59) | (int(height.group(1)) > 76)):
        print(height)
        return 0

    # Match hair color
    hair_color = re.search(r'(?:hcl:)(#[0-9a-f]+)', passport)
    if (hair_color == None):
        return 0
    elif (len(hair_color.group(1)) != 6):
        return 0

    # Match eyes color
    eye_color = re.search(r'(?:ecl:)(amb|blu|brn|gry|grn|hzl|oth)', passport)
    if eye_color == None:
        return 0

    # Match passport ID
    pass_id = re.search(r'(?:pid:)(\d+)', passport).group(1)
    if len(pass_id) != 9:
        return 0


# Read input from file
input_file = open("day4_input.txt", "r")
input_list = input_file.read().split("\n\n")


# ===Part 1===
count_valid1 = 0
for i in input_list:
    count_valid1 += find_field(i)

#print(count_valid1)


# ===Part 2===
count_valid2 = 0
for i in input_list:
    if find_field(i) == 1:
        count_valid2 += field_with_con(i)

print(count_valid2)