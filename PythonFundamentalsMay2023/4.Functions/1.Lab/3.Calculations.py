def multiply(a, b): return a * b


def divide(a, b): return int(a / b)


def add(a, b): return a + b


def subtract(a, b): return a - b


operation = input()
first_num = int(input())
second_num = int(input())

if operation == "multiply":
    print(multiply(first_num, second_num))
elif operation == "divide":
    print(divide(first_num, second_num))
elif operation == "add":
    print(add(first_num, second_num))
elif operation == "subtract":
    print(subtract(first_num, second_num))
