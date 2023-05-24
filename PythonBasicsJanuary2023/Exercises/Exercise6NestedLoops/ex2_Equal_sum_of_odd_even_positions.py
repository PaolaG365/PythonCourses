first_number, second_number = int(input()), int(input())

for number in range(first_number, second_number + 1):
    number_to_str = str(number)

    odds, evens = 0, 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            evens += int(digit)
        else:
            odds += int(digit)

    if evens == odds:
        print(number, end=' ')
