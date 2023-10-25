import sys

def calculate_score(rolls):
    total_score = 0
    frame = 0
    new_frame = True
    for index, roll in enumerate(rolls):
        if frame == 10:
            break
        if roll == 10:
            total_score += rolls[index + 1]
            total_score += rolls[index + 2]
            frame += 1
        elif not new_frame:
            if rolls[index - 1] + roll == 10:
                total_score += rolls[index + 1]
                frame += 1
            new_frame = True
        else:
            new_frame = False
        total_score += roll
    return total_score

if __name__ == '__main__':
    rolls = [int(x) for x in sys.argv[1:]]
    print(calculate_score(rolls))
