number = input()

max_num = float('-inf')

while number != "Stop":
    num = int(number)

    if num > max_num:
        max_num = num
    number = input()

print(max_num)
