#  ** Advent of Code 2022 **
#
#  --- Day 4: Camp Cleanup ---
#  The Elves have been assigned ranges of section IDs to clean up in a camp. They've noticed that
#  many of their assignments overlap and want to find the number of pairs in which one range fully
#  contains the other and the number of pairs that overlap at all. The challenge is to find out how
#  many pairs have one range fully containing the other (part 1). The Elves also want to know how
#  many pairs have any overlap at all (part 2).


def get_input(fileinput):
    try:
        cleanup_input = open(fileinput, "r")
        cleanup_data = cleanup_input.read()
        cleanup_pair_list = []
        for line in cleanup_data.splitlines():
            temp = line.split(",")
            cleanup_pair_list.append((separate_ranges(temp[0]), separate_ranges(temp[1])))
        return cleanup_pair_list
    finally:
        cleanup_input.close()


def separate_ranges(given_range):
    total_range = []
    range_pair = given_range.split("-")
    for i in range(len(range_pair)):
        range_pair[i] = int(range_pair[i])
    for i in range(range_pair[0], range_pair[1]+1):
        total_range.append(i)
    return total_range


def compare_ranges(pair_of_ranges):  # for complete overlap
    first_range = pair_of_ranges[0]
    second_range = pair_of_ranges[1]
    overlap_flag = 0
    if all(x in first_range for x in second_range):
        overlap_flag = 1
    elif all(x in second_range for x in first_range):
        overlap_flag = 1
    return overlap_flag


def count_complete_overlap_occurrences(given_ranges):
    count = 0
    for space in given_ranges:
        if compare_ranges(space) == 1:
            count += 1
    return count


def any_overlap_ranges(pair_of_ranges):
    first_range = pair_of_ranges[0]
    second_range = pair_of_ranges[1]
    overlap_flag = 0
    for space in first_range:
        if space in second_range:
            overlap_flag += 1
            break
    return overlap_flag


def count_overlap_occurrences(given_ranges):
    count = 0
    for space in given_ranges:
        if any_overlap_ranges(space) == 1:
            count += 1
    return count


if __name__ == "__main__":
    # Part 1
    print("There are", count_complete_overlap_occurrences(get_input("input/day_04.txt")),
          "occurences of overlapping cleaning spaces!")

    # Part 2
    print("There are", count_overlap_occurrences(get_input("input/day_04.txt")),
          "occurences of overlapping cleaning spaces!")
