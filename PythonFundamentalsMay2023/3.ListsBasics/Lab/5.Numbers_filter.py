lines = int(input())
special_numbers = []
sorted_numbers = []

for line in range(lines):
    number = int(input())
    special_numbers.append(number)

action = input()

if action == "even":
    for num in special_numbers:
        if num % 2 == 0:
            sorted_numbers.append(num)

if action == "odd":
    for num in special_numbers:
        if num % 2 != 0:
            sorted_numbers.append(num)

if action == "negative":
    for num in special_numbers:
        if num < 0:
            sorted_numbers.append(num)

if action == "positive":
    for num in special_numbers:
        if num >= 0:
            sorted_numbers.append(num)

print(sorted_numbers)
