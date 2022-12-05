data = open("inputday3.txt").readlines()
value = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
x = 0
threeGroup = []
totalSum = 0

if __name__ == "__main__":
    for line in data:
        if x < 2:
            x += 1
            threeGroup.append(list(dict.fromkeys(line.replace('\n', ''))))
        else:
            x = 0
            threeGroup.append(list(dict.fromkeys(line.replace('\n', ''))))
            # print(threeGroup)
            for letter in threeGroup[0]:
                if letter in threeGroup[1] and letter in threeGroup[2]:
                    for idx, place in enumerate(value):
                        if letter == place:
                            totalSum += (idx + 1)
                            break
                    break
            threeGroup = []
    print(totalSum)
