number = input()

for d1 in range(1, int(number[2]) + 1):
    for d2 in range(1, int(number[1]) + 1):
        for d3 in range(1, int(number[0]) + 1):
            print(f"{d1} * {d2} * {d3} = {d1 * d2 * d3};")
