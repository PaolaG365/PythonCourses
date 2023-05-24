n1, n2 = int(input()), int(input())
operation = input()

result = None

if operation == '+':
    result = f"{n1} {operation} {n2} = {n1 + n2}" + \
             (" - even" if (n1 + n2) % 2 == 0 else " - odd")

elif operation == "-":
    result = f"{n1} {operation} {n2} = {n1 - n2}" + \
             (" - even" if (n1 - n2) % 2 == 0 else " - odd")

elif operation == '*':
    result = f"{n1} {operation} {n2} = {n1 * n2}" + \
         (" - even" if (n1 * n2) % 2 == 0 else " - odd")

elif n2 == 0:
    result = f"Cannot divide {n1} by zero"

elif operation == "/":
    result = f"{n1} / {n2} = {n1 / n2:.2f}"

elif operation == "%":
    result = f'{n1} % {n2} = {n1 % n2}'

print(result)
