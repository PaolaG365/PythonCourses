num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
changes = 0

for d1 in range(num1, 9):
    for d2 in range(9, num2 - 1, -1):
        for d3 in range(num3, 9):
            for d4 in range(9, num4 - 1, -1):
                if d1 % 2 == 0 and d2 % 2 != 0 and d3 % 2 == 0 and d4 % 2 != 0:
                    if d2 != d4 or d1 != d3:
                        print(f"{d1}{d2} - {d3}{d4}")
                        changes += 1
                        if changes >= 6:
                            exit()
                    if d1 == d3 and d2 == d4:
                        print("Cannot change the same player.")
