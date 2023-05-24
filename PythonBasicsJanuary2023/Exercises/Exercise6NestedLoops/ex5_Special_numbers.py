n = int(input())

special_number = 0

for i in range(1111, 10_000):
    str_number = str(i)

    for index, digit in enumerate(str_number):
        divider = int(digit)

        if divider == 0:
            break
        elif n % divider == 0:
            special_number += 1

    if special_number == 4:
        print(i, end=" ")

    special_number = 0
