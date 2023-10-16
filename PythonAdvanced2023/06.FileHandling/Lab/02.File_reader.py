with open("numbers.txt", "r") as file:
    # total = 0
    # for line in file.readlines():
    #     total += int(line)
    print(sum(int(line) for line in file.readlines()))
    