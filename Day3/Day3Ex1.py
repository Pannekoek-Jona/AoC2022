data = open("inputday3.txt").readlines()
value = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

if __name__ == "__main__":
    totalSum = 0
    for line in data:
        line = line.replace('\n', '')
        sortedLine1 = sorted(line[:len(line) // 2])
        sortedLine2 = sorted(line[len(line) // 2:])
        # print(sortedLine1, sortedLine2)
        for letter in sortedLine1:
            if letter in sortedLine2:
                # print(letter)
                for idx, place in enumerate(value):
                    if letter == place:
                        totalSum += (idx + 1)
                        break
                break
    print(totalSum)
