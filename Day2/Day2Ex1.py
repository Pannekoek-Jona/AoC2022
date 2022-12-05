data = open("inputday2.txt").readlines()


# win 6
# same 3
# lose 0
# A/X rock 1
# B/Y paper 2
# C/Z scissors 3


def figurePoint(shape):
    if shape == 'X':
        point = 1
    elif shape == 'Y':
        point = 2
    else:
        point = 3
    return point


if __name__ == "__main__":
    points = 0
    for line in data:
        first = line[0]
        second = line[2]
        points += figurePoint(second)
        if first == 'A':
            if second == "X":
                points += 3
            elif second == 'Y':
                points += 6
        elif first == 'B':
            if second == "Y":
                points += 3
            elif second == 'Z':
                points += 6
        else:
            if second == 'Z':
                points += 3
            elif second == 'X':
                points += 6
    print(points)
