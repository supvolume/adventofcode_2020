"""Find the accumulator value before it run the second time"""

# Read input from file
input_file = open("day8_input.txt", "r")
input_list = input_file.read().split("\n")

# Create the list of instruction
all_instruction = []
for i in input_list:
    instruction = i.split(" ")
    all_instruction.append(instruction)


# Follow the instruction, change accumulator and location until the same line is read
accumulator = 0
location = 0
while all_instruction[location][0] != "done":
    if all_instruction[location][0] == "acc":
        accumulator += int(all_instruction[location][1])
        all_instruction[location][0] = "done"
        location += 1
    elif all_instruction[location][0] == "jmp":
        all_instruction[location][0] = "done"
        location += int(all_instruction[location][1])
    elif all_instruction[location][0] == "nop":
        all_instruction[location][0] = "done"
        location += 1

print(accumulator)