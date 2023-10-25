import sys

def calculate_score(rolls):
    total_score = 0
    frame = 1
    roll_index = 0

    while frame <= 10:
        if rolls[roll_index] == 10:
            total_score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:
            total_score += 10 + rolls[roll_index + 2]
            roll_index += 2
        else:
            total_score += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2

        frame += 1

    return total_score

if __name__ == "__main__":
    rolls = [int(x) for x in sys.argv[1:]]
    print(calculate_score(rolls))
