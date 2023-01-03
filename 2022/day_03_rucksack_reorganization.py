#  ** Advent of Code 2022 **
#
#  --- Day 3: Rucksack Reorganization ---
#
#  There are rucksacks with two compartments, each containing items of different types. Each item type has a
#  priority based on its letter, with lowercase letters having priorities 1 through 26 and uppercase letters
#  having priorities 27 through 52. One Elf did not follow the packing instructions, so some items need to
#  be rearranged. The goal is to find the item type that appears in both compartments of each rucksack and sum the
#  priorities of those item types (part 1).


def get_input(fileinput):
    try:
        rucksack_input = open(fileinput, "r")
        rucksack_data = rucksack_input.read()
        rucksack_list = []
        for line in rucksack_data.splitlines():
            rucksack_list.append(split_string(line))
    finally:
        rucksack_input.close()
    return rucksack_list


def split_string(string):
    first_half = ""
    second_half = ""
    for letter in string:
        if len(first_half) < len(string)//2:
            first_half += letter
        else:
            second_half += letter
    return first_half, second_half


def compare_compartments(compartments):
    new_list = []
    for first_half, second_half in compartments:
        for letter in first_half:
            occurrence = second_half.count(letter)
            if occurrence > 0:
                new_list.append(letter)
                break
    return new_list


def calculate_score(list_of_letters):
    score = 0
    letter_index = 'abcdefghijklmnopqrstuvwxyz'
    combined_letter_index = letter_index + letter_index.upper()
    letter_inventory = {}
    for letter in range(len(combined_letter_index)):
        letter_inventory.update({combined_letter_index[letter]: letter+1})
    for letter in list_of_letters:
        score += letter_inventory[letter]
    return score


if __name__ == "__main__":
    # Part 1
    print(calculate_score(compare_compartments(get_input("input/day_03.txt"))))
