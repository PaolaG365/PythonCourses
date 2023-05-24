n = int(input())

max_number = float('-inf')
total = 0

for i in range(n):
    number = int(input())
    total += number
    if number > max_number:
        max_number = number

without_max_num = total - max_number

if max_number == without_max_num:
    print(f"Yes\nSum = {max_number}")
else:
    print(f'No\nDiff = {abs(max_number - without_max_num)}')
