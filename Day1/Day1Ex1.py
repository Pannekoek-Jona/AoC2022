if __name__ == "__main__":
    docLines = []
    SubTotal = 0
    HighScore = 0
    with open('inputday1.txt') as my_file:
        for line in my_file:
            if line != '\n':
                SubTotal += int(line)
            else:
                if SubTotal > HighScore:
                    HighScore = SubTotal
                SubTotal = 0
    print(HighScore)
