#  ** Advent of Code 2022 **
#
#  --- Day 2: Rock Paper Scissors ---

#  Elves are setting up camp on a beach and are playing a Rock Paper Scissors tournament to determine the
#  placement of their tents. One Elf gives you an encrypted strategy guide to help you win. We are challenged
#  to calculate the total score if you follow the first strategy guide exactly (pt 1). The Elf changes the
#  strategy guide, and we are again challenged to find the new total score (part 2).

def get_input(fileinput):
    try:
        strategy_file = open(fileinput, "r")
        data = strategy_file.read()
        data = [list(line.split()) for line in data.splitlines()]  # StackOverflow code from user @tobias_k

    finally:
        strategy_file.close()
    return data

# X = rock = 1 = A = lose
# Y = paper = 2 = B = draw
# Z = scissors = 3 = C = win

def strategyInput(strategy_input):
    for round in strategy_input:
        if round[0] == 'A':
            round[0] = 'X'
        elif round[0] == 'B':
            round[0] = 'Y'
        else:
            round[0] = 'Z'
    return strategy_input

def secondStrategy(strategy_input):
    for round in strategyInput(strategy_input):
        if round[1] == 'Y':
            round[1] = round[0]
        elif round[1] == 'Z':
            if round[0] == 'X':
                round[1] = 'Y'
            elif round[0] == 'Y':
                round[1] = 'Z'
            else:
                round[1] = 'X'
        else:
            if round[0] == 'X':
                round[1] = 'Z'
            elif round[0] == 'Y':
                round[1] = 'X'
            else:
                round[1] = 'Y'
    return strategy_input


def calculateTotalScore(strategy_input, strategy):
    # 0 for loss, 3 for draw, 6 for win
    data = strategyInput(strategy_input) if strategy == 1 else secondStrategy(strategy_input)
    score = 0
    for round in data:
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
    print(calculateTotalScore(get_input("input/day_02.txt"), 1))
    print(calculateTotalScore(get_input("input/day_02.txt"), 2))