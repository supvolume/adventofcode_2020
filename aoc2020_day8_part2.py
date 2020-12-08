"""Find where to change jmp to nop or nop to jmp, and get the accumulator value after it terminates"""

import copy


# Check if follow the instruction the same line is read or not
def check_loop(all_instruction):
    all_inst = copy.deepcopy(all_instruction)
    accumulator = 0
    location = 0
    while (location < len(all_inst)) and (all_inst[location][0] != "done"):
        if all_inst[location][0] == "acc":
            accumulator += int(all_inst[location][1])
            all_inst[location][0] = "done"
            location += 1
        elif all_inst[location][0] == "jmp":
            all_inst[location][0] = "done"
            location += int(all_inst[location][1])
        elif all_inst[location][0] == "nop":
            all_inst[location][0] = "done"
            location += 1
    # If the location is more than length of instruction, it mean the process is terminate normally
    if location >= len(all_inst):
        return "not loop", accumulator
    else:
        return "loop", accumulator


# Read input from file
input_file = open("day8_input.txt", "r")
input_list = input_file.read().split("\n")

# Create the list of instruction
all_instruction = []
for i in input_list:
    instruction = i.split(" ")
    all_instruction.append(instruction)

for i in range(len(all_instruction)):
    # Change "jmp" to "nop"
    if all_instruction[i][0] == "jmp":
        all_instruction[i][0] = "nop"
        # Check if the instruction is still in loop or not
        loop_sta, accumulator = check_loop(all_instruction)
        if loop_sta == "not loop":
            print(accumulator)
            break
        else:
            # Change value back
            all_instruction[i][0] = "jmp"
    # Change "nop" to "jmp"
    elif all_instruction[i][0] == "nop":
        all_instruction[i][0] = "jmp"
        # Check if the instruction is still in loop or not
        loop_sta, accumulator = check_loop(all_instruction)
        if loop_sta == "not loop":
            print(accumulator)
            break
        else:
            # Change value back
            all_instruction[i][0] = "nop"
