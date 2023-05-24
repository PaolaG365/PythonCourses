number = int(input())
magic_numbers = [5, 7, 11]
SPECIAL_NUMBER = False

for num in range(1, number + 1):
    str_num = str(num)
    el_sum = 0

    for el in range(len(str_num)):
        el_sum += int(str_num[el])
        if el_sum in magic_numbers:
            SPECIAL_NUMBER = True
        else:
            SPECIAL_NUMBER = False

    print(f"{num} -> {SPECIAL_NUMBER}")
