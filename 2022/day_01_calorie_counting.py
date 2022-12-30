#  ** Advent of Code 2022 **
#
#  --- Day 1: Calorie Counting ---

#  Santa's reindeer need to eat star fruit to have enough magical energy to deliver presents on Christmas.
#  The Elves go on an annual expedition to retrieve at least 50 of these stars from a jungle grove. The
#  Elves take inventory of the food they are carrying, listing the calories for each item. We are challenged
#  to find the Elf carrying the most calories and answer with the total number of calories they are carrying.


def get_input(fileinput):
    try:
        calories_file = open(fileinput, "r")
        calories_data = calories_file.read()
        all_the_calories = calories_data.split("\n")
        calories_per_elf = []
        temp = []
        for calories in all_the_calories:
            if calories != '':
                temp.append(int(calories))
            else:
                calories_per_elf.append(sum(temp))
                temp = []

    finally:
        calories_file.close()

    return calories_per_elf


if __name__ == "__main__":
    highest_calorie_amount = max(get_input("input/day_01.txt"))
    elf = get_input("input/day_01.txt").index(highest_calorie_amount)
    print("Elf number", elf+1, "is carrying the most calories. This Elf is carrying as much as", highest_calorie_amount, "calories!!")
