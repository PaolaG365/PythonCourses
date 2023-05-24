number = input()

min_num = float('inf')

while number != "Stop":
    num = int(number)

    if num < min_num:
        min_num = num
    number = input()

print(min_num)
