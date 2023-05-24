number1 = int(input())

sum_number = 0

while sum_number <= number1:
    number = int(input())
    sum_number += number
    if sum_number == number1:
        break
print(sum_number)
