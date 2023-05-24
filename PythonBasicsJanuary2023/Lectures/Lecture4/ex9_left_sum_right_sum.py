n = int(input())

total1, total2 = 0, 0

for number in range(n*2):
    number_to_add = int(input())
    if number < n:
        total1 += number_to_add
    elif number >= n:
        total2 += number_to_add

if total1 == total2:
    print(f"Yes, sum = {total1}")
else:
    print(f'No, diff = {abs(total1 - total2)}')
