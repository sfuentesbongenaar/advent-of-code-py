#  ** Advent of Code 2022 **
#
#  --- Day 2: Rock Paper Scissors ---

#  Elves are setting up camp on a beach and are playing a Rock Paper Scissors tournament to determine the
#  placement of their tents. One Elf gives you an encrypted strategy guide to help you win. We are challenged
#  to calculate the total score if you follow the strategy guide exactly (pt 1).

def get_input(fileinput):
    try:
        strategy_file = open(fileinput, "r")
        data = strategy_file.read()
        data = [list(line.split()) for line in data.splitlines()]  # StackOverflow code from user @tobias_k

    finally:
        strategy_file.close()
    return data

def strategyInput(strategy_input):
    # X = rock = 1 = A
    # Y = paper = 2 = B
    # Z = scissors = 3 = C
    for round in strategy_input:
        if round[0] == 'A':
            round[0] = 'X'
        elif round[0] == 'B':
            round[0] = 'Y'
        else:
            round[0] = 'Z'
    return strategy_input

def calculateTotalScore(strategy_input):
    # 0 for loss, 3 for draw, 6 for win
    score = 0
    for round in strategyInput(strategy_input):
        if round[0] == round[1]:
            score += 3
        elif round[0] == 'X' and round[1] == 'Y':
            score += 6
        elif round[0] == 'Y' and round[1] == 'Z':
            score += 6
        elif round[0] == 'Z' and round[1] == 'X':
            score += 6
        if round[1] == 'X':
            score += 1
        elif round[1] == 'Y':
            score += 2
        elif round[1] == 'Z':
            score += 3
    return score


if __name__ == "__main__":
    print(calculateTotalScore(get_input("input/day_02.txt")))