number1, number2 = int(input()), int(input())
print(f"Before: \na = {number1}\nb = {number2}")

number1, number2 = number2, number1
print(f"After: \na = {number1}\nb = {number2}")
