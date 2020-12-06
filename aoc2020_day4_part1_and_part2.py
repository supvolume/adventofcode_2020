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

    birth_y = re.search(r'(?:byr:)(\d+)', passport)
    if birth_y is None:
        return 0
    elif not ((int(birth_y.group(1)) >= 1920) & (int(birth_y.group(1)) <= 2002)):
        return 0

    # Match issue year
    issue_y = re.search(r'(?:iyr:)(\d+)', passport)
    if issue_y is None:
        return 0
    elif not ((int(issue_y.group(1)) >= 2010) & (int(issue_y.group(1)) <= 2020)):
        return 0

    # Match expiration year
    exp_y = re.search(r'(?:eyr:)(\d+)', passport)
    if exp_y is None:
        return 0
    elif not ((int(exp_y.group(1)) >= 2020) & (int(exp_y.group(1)) <= 2030)):
        return 0

    # Match height
    height = re.search(r'(?:hgt:)(\d+)(cm|in)', passport)
    if height is None:
        return 0
    elif height.group(2) == "cm":
        if not ((int(height.group(1)) >= 150) & (int(height.group(1)) <= 193)):
            return 0
    elif height.group(2) == "in":
        if not ((int(height.group(1)) >= 59) & (int(height.group(1)) <= 76)):
            return 0

    # Match hair color
    hair_color = re.search(r'(?:hcl:)(#[0-9a-f]+)', passport)
    if hair_color is None:
        return 0
    elif len(hair_color.group(1)) != 7:
        return 0

    # Match eyes color
    eye_color = re.search(r'(?:ecl:)(amb|blu|brn|gry|grn|hzl|oth)', passport)
    if eye_color is None:
        return 0

    # Match passport ID
    pass_id = re.search(r'(?:pid:)(\d+)', passport)
    if pass_id is None:
        return 0
    elif len(pass_id.group(1)) != 9:
        return 0
    return 1


# Read input from file
input_file = open("day4_input.txt", "r")
input_list = input_file.read().split("\n\n")


# ===Part 1===
count_valid1 = 0
for i in input_list:
    count_valid1 += find_field(i)
print("Part 1 answer: ", count_valid1)


# ===Part 2===
count_valid2 = 0
for i in input_list:
    if find_field(i) == 1:
        count_valid2 += field_with_con(i)
print("Part 2 answer: ", count_valid2)
