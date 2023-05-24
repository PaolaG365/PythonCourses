n = int(input())

odd_numbers, even_numbers = 0, 0

for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even_numbers += number
    else:
        odd_numbers += number

if odd_numbers == even_numbers:
    print(f'Yes\nSum = {odd_numbers}')
else:
    print(f'No\nDiff = {abs(odd_numbers - even_numbers)}')
