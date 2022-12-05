data = open("inputday2.txt").readlines()
# win 6 = Z
# same 3 = Y
# lose 0 = X
# A rock 1
# B paper 2
# C scissors 3


if __name__ == "__main__":
    points = 0
    steen = 1
    papier = 2
    schaar = 3
    win = 6
    draw = 3
    for line in data:
        first = line[0]
        second = line[2]
        if first == 'A':  # steen
            if second == "Z":
                points += win
                points += papier
            elif second == 'Y':
                points += draw
                points += steen
            else:
                points += schaar
        elif first == 'B':  # papier
            if second == "Z":
                points += win
                points += schaar
            elif second == 'Y':
                points += draw
                points += papier
            else:
                points += steen
        else:  # schaar
            if second == 'Z':
                points += win
                points += steen
            elif second == 'Y':
                points += draw
                points += schaar
            else:
                points += papier
    print(points)
