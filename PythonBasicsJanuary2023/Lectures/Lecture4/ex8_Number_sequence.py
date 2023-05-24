import sys

n = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize

for _ in range(n):
    number = int(input())

    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print(f'Max number: {max_number}\nMin number: {min_number}')
